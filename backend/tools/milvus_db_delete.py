from pymilvus import connections, utility, Collection

# 连接到 Milvus
connections.connect(alias="default", host="127.0.0.1", port="19530")

# 删除集合
collection_name = "economics_only_name"  # 替换成你的集合名

utility.drop_collection(collection_name)

print(f"Collection {collection_name} has been deleted.")


# from pymilvus import connections, utility

# 连接到 Milvus 服务
# connections.connect("default", host="localhost", port="19530")

# 检查集合是否存在
# collection_name = "ceconomics_only_name"
exists = utility.has_collection(collection_name)

if exists:
    print(f"Collection '{collection_name}' exists.")
else:
    print(f"Collection '{collection_name}' has been deleted or does not exist.")

collection = Collection(collection_name)

print(collection.schema)