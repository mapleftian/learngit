### 零碎知识点

1. DataFrame可以与字典Dict进行直接转换
2. dataFrame删除使用drop时，返回一个新的对象，并不是直接删除原数据内容
3. 创建时就可以对列及行进行命名。如index=？？，column=？？
4. pandas 在判断一个series里面是否包含某元素时候要加tolist（）

```python
'3962302' in df['CLIENT_ID'].tolist()
```

