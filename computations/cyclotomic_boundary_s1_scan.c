/* cyclotomic_boundary_s1_scan.c — exact scan of the condition c | a1 for
 * conj:cyclotomic-boundary-at-keystone, far past what the Python producer reaches.
 *
 * For n = T_j + r (1 <= r <= j, non-triangular), c = C(j+1, r) and
 *   a1/c = -4j - 2 + 2r(j-r)/(j+1) + j(j+2)/(r+1) + (j+2)^2/(j-r+2),
 * so c | a1 iff D1 | N1 with D1 = (j+1)(r+1)(j-r+2) and N1 the numerator below.
 * The identity is checked against the closed form in cyclotomic_boundary_power_sum.py.
 * Integer arithmetic only (__int128; N1 < 2^100 for j <= 10^6).
 *
 * Build and run:  cc -O2 -o /tmp/s1scan computations/cyclotomic_boundary_s1_scan.c
 *                 /tmp/s1scan 400000        (about 10 minutes)
 * Prints every (j, r) with c | a1; each must then be checked for c | 2 a2 in Python.
 */
#include <stdio.h>
#include <stdlib.h>
typedef __int128 i128;
int main(int argc, char **argv) {
  long J = argc > 1 ? atol(argv[1]) : 20000, cnt = 0;
  if (J > 1000000) { fprintf(stderr, "J > 10^6 may overflow\n"); return 1; }
  for (long j = 4; j <= J; j++)
    for (long r = 1; r <= j; r++) {
      i128 A = j + 1, B = r + 1, C = j - r + 2;
      i128 n1 = (i128)2 * r * (j - r) * B * C + (i128)j * (j + 2) * A * C
              + (i128)(j + 2) * (j + 2) * A * B;
      if (n1 % (A * B * C) == 0) { printf("%ld %ld\n", j, r); fflush(stdout); cnt++; }
    }
  fprintf(stderr, "j <= %ld: %ld solutions\n", J, cnt);
  return 0;
}
