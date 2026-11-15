---
doc_id: arxiv-2408.04921v2
doc_title: "IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP"
section_id: sec-006-appendix-b-theorem-39
section_title: "Appendix B. Theorem 3.9"
section_number: null
pages: 22-24
source_pdf: 2408.04921v2.pdf
source_sha256: dcfe112640a8adda
toc_source: outline
doc_brief: "IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP — The paper studies how to compute irreducible characters of the generalized symmetric group Ck ≀Sn by iterative algorithms."
---
# Take k=3, n=5
P=PartitionTuples(3,5)
import random
lam=random.choice(P)
rho=random.choice(P)
print(lam,rho)
# Set environment
IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP
23
s=max(max(lam))
j=lam.index(max(lam))
r=Zmod(3)
w=SR.var(’w’)
def sub(nums):
res = [[]]
for num in nums:
res += [ i + [num] for i in res]
return res
import itertools
array1 = sub(rho[0])
array2 = sub(rho[1])
array3 = sub(rho[2])
combs = itertools.product(array1,array2,array3)
# Simulate the path
import copy
class Solution:
def subsets(self, nums):
result = []
path = []
self.backtracking(nums, 0, path, result)
return result
def backtracking(self, nums, startIndex, path, result):
result.append(path[:])
for i in range(startIndex, len(nums)):
path.append(nums[i])
self.backtracking(nums, i + 1, path, result)
path.pop()
# Filter out rho satisfying conditions
for comb in combs:
if sum(comb[0])+sum(comb[1])+sum(comb[2])<=5-s:
box0 = comb[0]
box1 = comb[1]
box2 = comb[2]
taus=
Partitions(5-s-sum(comb[0])-sum(comb[1])-sum(comb[2])).list()
solu=Solution()
result = {}
for tau in taus:
d=Partition(tau).centralizer_size()
24
HUIMIN GAO AND NAIHUAN JING
c=(-1/3)^len(tau)/d*w^r(-(len(rho[1])-
len(comb[1]))*1*j-(len(rho[2])-len(comb[2]))*2*j)
all_index_3 = list(range(len(tau)))
all_index_1 = solu.subsets(all_index_3)
for i_i in range(len(all_index_1)):
index_2_3 =
list(set(all_index_3)-set(all_index_1[i_i]))
all_index_2_3 = solu.subsets(index_2_3)
box0_i_index = copy.deepcopy(all_index_2_3)
box1_i_index = copy.deepcopy(all_index_2_3)
box2_i_index = copy.deepcopy(all_index_2_3)
for i_i_i in range(len(all_index_2_3)):
box0_i_index[i_i_i] =
list(set(all_index_3)-set(index_2_3))
box1_i_index[i_i_i] =
list(set(index_2_3)-set(all_index_2_3[i_i_i]))
for k_0 in range(len(box0_i_index[i_i_i])):
box0_i_index[i_i_i][k_0] =
tau[box0_i_index[i_i_i][k_0]]
for k_1 in range(len(box1_i_index[i_i_i])):
box1_i_index[i_i_i][k_1] =
tau[box1_i_index[i_i_i][k_1]]
for k_2 in range(len(box2_i_index[i_i_i])):
box2_i_index[i_i_i][k_2] =
tau[box2_i_index[i_i_i][k_2]]
coff =c*( w^r((len(box0_i_index[i_i_i]) * 0 +
len(box1_i_index[i_i_i]) * 1 +
len(box2_i_index[i_i_i]) * 2)*j))
x = box0 + box0_i_index[i_i_i]
y = box1 + box1_i_index[i_i_i]
z = box2 + box2_i_index[i_i_i]
tmp = list()
tmp.append(x)
tmp.append(y)
tmp.append(z)
result["rho"] = tmp
print(coff,"new rho:",result["rho"])
School of Mathematics, South China University of Technology, Guangzhou,
Guangdong 510640, China
Email address: 13144508207@163.com
Department of Mathematics, North Carolina State University, Raleigh,
NC 27695, USA
Email address: jing@ncsu.edu
