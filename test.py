def test_main():
    count:int = 10
    arr:list[int] = []
    if count <= 0:
        return {"array":[]}
    for i in range(0,count):
        arr.append(i)
    
    assert len(arr) == 10