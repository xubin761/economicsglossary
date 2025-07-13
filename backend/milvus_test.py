from pymilvus import connections

# 连接到本地的 Milvus 服务
connections.connect(host='localhost', port='19530')

# 确保连接成功
if connections.has_connection("default"):
    print("Connected to Milvus successfully!")

from pymilvus import Collection, FieldSchema, DataType, CollectionSchema
import numpy as np

# 定义字段：主键 ID 和 128 维浮动向量字段
field_id = FieldSchema(name="id", dtype=DataType.INT64, is_primary=True)  # 主键字段
field_vector = FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=128)  # 向量字段

# 创建 CollectionSchema，包含字段列表
schema = CollectionSchema(fields=[field_id, field_vector])

# 创建集合并传入 schema
collection = Collection(name="example_collection", schema=schema)

# 生成随机向量数据
vectors = np.random.random((10, 128)).astype(np.float32)

# 插入数据
data = [
    [i for i in range(10)],  # 生成 ID 数据
    vectors  # 向量数据
]
collection.insert(data)

# 创建索引
index_params = {
    "index_type": "IVF_FLAT",  # 选择索引类型，可以选择 IVF_FLAT, IVF_SQ8, HNSW, 等
    "metric_type": "L2",  # 距离度量方式，L2 表示欧几里得距离
    "params": {"nlist": 128}  # 索引的具体参数，这里使用 nlist
}
collection.create_index(field_name="vector", index_params=index_params)

# 确保集合已经加载
collection.load()

# 生成一个随机查询向量
query_vector = np.random.random((1, 128)).astype(np.float32)

# 执行搜索
search_results = collection.search(query_vector, "vector", limit=5, param={"nprobe": 10})

# 打印搜索结果
for result in search_results[0]:  # search_results[0] 是一个列表，包含每个查询的结果
    print(f"ID: {result.id}, Distance: {result.distance}")

connections.disconnect("default")



