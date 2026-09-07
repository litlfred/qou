---
doc_id: exploring-the-geometric-buchberger-algorithm-in-integer-prog
doc_title: "Exploring the Geometric Buchberger Algorithm in Integer Programming Gabriel Mattos Langeloh gmlangeloh@inf.ufrgs.br"
section_id: sec-006-42-evaluating-the-binary-case
section_title: "Evaluating the binary case"
section_number: 4.2
pages: 5-6
source_pdf: Exploring the Geometric Buchberger Algorithm in Integer Programming.pdf
source_sha256: 73854bc5e3bcffb0
doc_brief: "Exploring the Geometric Buchberger Algorithm in Integer Programming Gabriel Mattos Langeloh gmlangeloh@inf.ufrgs.br — The Geometric Buchberger algorithm is a specialization of the clas- sical"
---
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
ISSAC 24, July 16-19, 2024, Raleigh, NC, USA

Problem n m_  t(%) mem(%) #Rs (%)
0-1KP 5 1 75.69 99.08 77.25,
0-1KP 10 1 56.75 85.80 72.36
0-1KP 20 1 83.10 72.74 72.37
0-1KP 30 1 77.78 67.56 68.98
0-1KP 40 1 85.75 68.44 69.23
0-1KP 50 1 94.14 74.98 75.50
0-1MDKP 10 2 60.69 81.09 60.72
0-1MDKP 10 3 56.36 66.33 49.80
0-1MDKP 10. 4 52.75 67.08 49.27
0-1MDKP 10 5 54.52 54.65 42.78
0-1MDKP 15 2 66.92 55.53 51.68
0-1MDKP 15 3 59.36 46.67 45.24
0-1MDKP 15 4 58.84 39.90 37.33
0-1MDKP 15 5 51.36 31.56 28.88
0-1MDKP 20 2 69.96 55.33 55.95
0-IMDKP 20 3. 52.20 38.37 37.69
0-IMDKP 20 4 = 55.72 32.74 31.74
0-1MDKP 20 5 60.29 27.00 25.53
0-1MDKP 25 2 67.94 54.16 54.18
0-1MDKP 25 3 66.46 41.61 40.88
SCP 30 15 17.93 17.22 7.58
SCP 30 16 19.51 22.02 9.85
SCP 30 17 30.06 12.43 4.77
SCP 30 18 37.28 12.68 5.92
SCP 30 19 28.58 13.30 8.99
SPP 100 25 50.28 59.52 28.42
SPP 100 30 47.34 46.88 21.45
SPP 100 35 77.44 35.22 24.34

Table 2: Percentage of time (t), memory (mem) and number
of reductions (#Rs) of IPGBs with the binary truncation cri-
terion in relation to the same data obtained by IPGBs-NC
(no-criterion).

criteria. Even so, the use of this criterion leads to speedups of about
100% to 500%.
