import time
M = 4
N = 2
start_time = time.time()
for i in range(M):
    print(i)
    time.sleep(1)
    for j in range(N):
        print(j)
        time.sleep(1)

end_time = time.time()


total_time = end_time - start_time
print(total_time)