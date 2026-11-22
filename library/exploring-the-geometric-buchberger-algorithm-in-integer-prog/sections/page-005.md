---
doc_id: exploring-the-geometric-buchberger-algorithm-in-integer-prog
doc_title: "Exploring the Geometric Buchberger Algorithm in Integer Programming"
section_id: page-005
section_title: "Page 5"
pages: 5-5
pdf_page: 5
source_pdf: Exploring the Geometric Buchberger Algorithm in Integer Programming.pdf
source_sha256: 73854bc5e3bcffb0
text_source: ocr
granularity: page
doc_brief: "exploring-the-geometric-buchberger-algorithm-in-integer-prog — 8 sections: Page 1; Page 2; Page 3"
---
Exploring the Geometric Buchberger Algorithm in Integer Programming,

ISSAC ’24, July 16-19, 2024, Raleigh, NC, USA

IPGBs-NC IPGBs 4ti2
Problem nom |G| t(s) mem(GB)  #Reductions t(s) mem(GB) #Reductions t (s)
0-1KP 5 1 20.40 0.01 0.00 48.80 0.01 0.00 37.70 0.02
0-1KP 10 1 105.20 0.01 0.00 1130.80 0.01 0.00 818.20 0.03
0-1KP 20 1 972.60 0.05 0.02 81189.10 0.04 0.01 58755.80 0.17
0-1KP 30 1 6301.40 2.69 0.62 4134558.20 2.09 0.42 2852043.10 5.52
0-1KP 40 1 18153.60 38.32 5.44 37787790.40 32.86 3.72 26161116.50 72.46
0-1KP 50 1 34642.10 140.35 16.90 118704565.10 132.12 12.67 89624182.30 260.93
0-1MDKP 10 2 181.40 0.01 0.00 3599.20 0.01 0.00 2185.30 0.04
0-1MDKP 10 3 309.50 0.02 0.00 8693.10 0.01 0.00 4329.50 0.05
0-1MDKP 10 4 348.40 0.02 0.00 8595.30 0.01 0.00 4234.60 0.06
0-1MDKP 10 5 531.10 0.03 0.01 15073.80 0.01 0.00 6448.30 0.09
0-1MDKP 15 2 906.90 0.07 0.02 99440.90 0.04 0.01 51392.00 0.20
0-1MDKP 15 3 1545.80 0.16 0.04 226314.40 0.09 0.02 102388.90 0.44
0-1MDKP 15 4 2342.90 0.33 0.08 418772.20 0.20 0.03 156329.70 0.81
0-1MDKP 15 5 4135.20 1.01 0.19 950859.60 0.52 0.06 274643.60 2.05
0-IMDKP 20 2 2946.00 0.62 0.15 909352.50 0.44 0.08 508780.70 1.32
0-IMDKP 20 3 9619.20 9.69 1.47 9917221.90 5.06 0.57 3738125.60 16.14
0-IMDKP 20 4 = 17601.50 39.01 3.89 26157794.10 21.74 1.27 8303001.10 52.10
0-1MDKP 20 5 32115.10 136.16 10.03 66915780.60 82.09 2.71  17084041.50 152.12
0-1MDKP 25 2  10895.60 9.59 1.67 11376734.50 6.52 0.90 6163731.00 16.86
0-IMDKP = 25 3  26846.70 107.17 9.89  69293852.60 71.22 4.12 28328019.00 139.97
SCP 30 15 3241.40 7.82 0.47 847420.60 1.40 0.08 64244.90 8.56
SCP 30 16 3345.10 5.50 0.37 732227.50 1.07 0.08 72114.50 6.37
SCP 30 17° 19739.30 199.87 5.41 15726902.00 60.07 0.67 750251.70 156.40
SCP 30 18 30552.80 574.58 10.76  30865634.30 214.23 1.36 1828173.90 423.80
SCP 30 19 13758.00 115.53 3.61 12963816.50 33.01 0.48 1165391.00 97.94
SPP 100 25 2999.00 2.08 0.33 321619.50 1.05 0.20 91397.40 5.59
SPP 100 30 13386.70 44.23 3.54 4650716.50 20.94 1.66 997624.50 80.31
SPP 100 35 67121.00 1409.84 65.46 59968119.00 1091.79 23.05 14594744.00 1784.00

Table 1: Results for full Grébner basis computation of binary instances. IPGBs-NC (no criterion) corresponds to the results of
IPGBs without the binary truncation criterion of Corollary 3.3 while IPGBs corresponds to results including that criterion. All
results are the averages over 10 random instances generated for each set of parameters n, m.

least moderately difficult for Grébner basis methods. All reported
Grébner basis computations are b-truncated according to the value
of b given in the input integer program for both IPGBs and 4ti2.
Below is a brief description of each of these problems as integer
programs along with how the data for each of them was generated.

Knapsacks: max{c!x | Ax < b, x € D}, where D = {0,1}" for
binary variants and D = Z? for unbounded variants. Furthermore,
for multiknapsacks, the constraint matrix A has at least 2 rows,
while for simple knapsacks, A is a single row matrix. All instances
were generated randomly with c;, Ajj € [0,1000]  Z for all i €
[m], j € [n] and bj = 3 D7, Aij for alli € [m].

Set packing: max{1),x | A(U)x < In, x € {0,1}"}, where U is
a collection of m subsets of [n] where each element of [n] appears
with a fixed probability of p = 0.05, and A(U)j;j = 1 if i € [n] is in
the j-th set of U, and A(U);; = 0 otherwise.

Set cover: min{1) x | A(U)Tx > 1m, x € {0,1}"}, where U and
A(U) have the same interpretation as in set packing and p = 0.2
instead.

338

4.2 Evaluating the binary case

In order to evaluate the effectiveness of the binary improvements
proposed in Section 3, we ran IPGBs both with and without the
binary truncation criterion of Corollary 3.3. Tables 1 and 2 show
the results of this experiment for each family of instances.

From Table 1, it is clear that IPGBs-NC, the version of IPGBs
without the binary truncation criterion, performs worse than full
IPGBs in every single case in terms of time, total memory use and
number of reductions. Table 2 shows that the binary truncation
criterion decreases the number of reductions by at least about 20%
for every case. Furthermore, this decrease is significantly higher
for set cover and set packing, reaching about 95% fewer S-vectors
reduced in the best cases.

It is also clear from Table 2 that a decrease in the number of
reductions does not necessarily lead to a decrease in running time
of the same magnitude. This is expected, since the application of the
binary truncation criterion itself has a significant cost because it is
applied to every S-vector not eliminated by the GCD or cancellation
