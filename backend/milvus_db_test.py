from pymilvus import connections, Collection
import numpy as np

# 连接到 Milvus
connections.connect(alias="default", host="127.0.0.1", port="19530")

# 定义集合名称
collection_name = "economics_only_name"

# 创建集合对象
collection = Collection(collection_name)

# 加载集合
collection.load()
print(f"Collection {collection_name} has been loaded.")

# 获取集合的 schema，检查向量字段的维度
print("Collection schema:", collection.schema)

# 生成查询向量，维度应与集合中的向量维度一致
query_vectors = np.random.rand(1, 1024).tolist()  # 假设集合维度是 1024，生成一个查询向量

# 执行搜索操作
search_result = collection.search(
    data=query_vectors,  # 查询向量
    anns_field="vector",  # 向量字段
    param={"nprobe": 10},  # 搜索参数
    limit=10  # 返回的结果数量
)

# 输出搜索结果
print(search_result)
