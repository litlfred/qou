# Keystone value map (s013): q-Bessel Tricomi C_{0,q} sub-route refuted — now with an in-repo source

**Date:** 2026-07-04
**Bean:** [`s013`](../../.beans/s013--keystone-value-map-colored-lawrence-rozansky-s-mat.md)
**Follows:** [`2026-07-04-keystone-valuemap-target-is-compact-hecke.md`](2026-07-04-keystone-valuemap-target-is-compact-hecke.md) (PR #3292 — target is compact Hecke; multi-arg q-Bessel needs the un-uploaded Plancherel kernel) and [`2026-07-02-keystone-valuemap-qbessel-gate.md`](2026-07-02-keystone-valuemap-qbessel-gate.md) §4 (single-arg q-Bessel row refuted, un-sourced at the time)
**Source (owner upload):** `library/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials.pdf` — Raza N., Fadel M., Cesarano C., "On 2-variable q-Legendre polynomials: the view point of the q-operational technique", *Carpathian Math. Publ.* 2025, **17**(1) 14–26, doi:10.15330/cmp.17.1.14-26.
**Script:** [`computations/probes/keystone_qbessel_tricomi_c0q_nodes.py`](../../computations/probes/keystone_qbessel_tricomi_c0q_nodes.py)
**Witness:** [`computations/probes/keystone-qbessel-tricomi-c0q-nodes.witness.json`](../../computations/probes/keystone-qbessel-tricomi-c0q-nodes.witness.json)
**Status:** one (a)-scope refutation, now carrying an in-repo source. No fit; nothing wired.

## What the upload actually is

PR #3292 established that the surviving q-Bessel lead (redirect ii) was not
disciplined-actionable in-repo because the falsifiable multi-argument E_q(2)
vacuum row needs its radial arguments fixed by the **Koelink–Swarttouw q-Hankel
Plancherel kernel**, which was not in `library/`. The owner then uploaded
`library/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials.pdf`.

That paper is a **q-Bessel source but not the Plancherel source**: it *cites*
Koornwinder–Swarttouw (its ref [22]) in the bibliography but does not contain
the q-Hankel transform, the E_q(2) Plancherel measure, or the J^{(3)}
orthogonality zeros. Text scan: 0 occurrences of `plancherel`, `E_q(2)`,
`vacuum`, `measure`, `norm`; 1 of `recurrence`. It *does* give, as a clean
parameter-free series (its eq. (11); convention 0 < q < 1, [k]_q = (1−q^k)/(1−q)):

$$
C_{0,q}(x) \;=\; \sum_{k\ge 0}\frac{(-1)^k x^k}{([k]_q!)^2},
\qquad\text{entire (converges }\forall x\text{)},
$$

the **0th-order q-Bessel Tricomi function**, with $C_{0,q}(x)$ the q-analog of
$J_0(2\sqrt{x})$ (paper eq. (10)). Because $C_{0,q}$ is entire and depends only
on $q$, its positive real zeros $\{\xi_1 < \xi_2 < \dots\}$ and its values at
q-integer nodes are **fixed by $q$ alone** — 0 free parameters. So a genuinely
falsifiable check *is* constructible from this upload, even though the
argument-fixing Plancherel measure is not.

## The 0-dof test and its result

At the substrate ($q = q_0^{-1} \approx 0.90092$, the $|q|<1$ image of the
categorical $q_0 > 1$), the first five positive zeros of $C_{0,q}$ are

| $j$ | $\xi_j$ | $\sqrt{\xi_j}$ | $\xi_j/\xi_1$ |
|--:|--:|--:|--:|
| 1 | 1.52740 | 1.23588 | 1 |
| 2 | 8.16779 | 2.85793 | 5.34752 |
| 3 | 20.6072 | 4.53952 | 13.4917 |
| 4 | 39.7066 | 6.30132 | 25.9963 |
| 5 | 66.7409 | 8.16951 | 43.6958 |

The compact keystone target is
$\mathrm{bwS0} = \{[1]_q,\,[4]_q,\,[5]_q,\,[4]_q[3]_q/[2]_q\}
\approx \{1,\,4.10968,\,5.22044,\,6.22044\}$ (balanced q-integers at $q_0$;
PR #3292 FACT 1). Testing **every** parameter-free quantity of $C_{0,q}$ — the
ordered zeros $\xi_j$, their roots $\sqrt{\xi_j}$, the non-trivial normalisations
$\xi_j/\xi_1$ and $\sqrt{\xi_j/\xi_1}$ ($j\ge 2$), the consecutive gaps
$\xi_{j+1}-\xi_j$, and $C_{0,q}$ evaluated at the nodes $[n]_q$ and $n$
($n = 1..5$) — against the three **non-trivial** targets:

- **No match within 1%.** The nearest approaches are $\xi_2/\xi_1 = 5.348$ vs
  $[5]_q = 5.220$ (2.4% off) and $\sqrt{\xi_4} = 6.301$ vs
  $[4][3]/[2] = 6.220$ (1.3% off) — both outside the 1% gate.
- **The ordered 4-vector does not match** ($\sqrt{\xi_j}$, $\xi_j/\xi_1$, or
  $\xi_j$ read as a 4-vector).

(The degenerate identity $\xi_1/\xi_1 = 1 = [1]_q$ is excluded from the gate: it
holds for *any* function's first zero and carries no content.)

## Verdict — scope (a), sourced

**REFUTED-as-is (scope a):** no parameter-free quantity of the sourced
0th-order q-Bessel Tricomi $C_{0,q}$ reproduces the compact keystone value-map
target at its own natural nodes. This is exactly what PR #3292's type argument
predicts — a transcendental, non-compact q-Bessel object does not land on the
compact **algebraic** (Laurent-polynomial) target at parameter-free nodes.

What this **does** buy: the q-Bessel-Tricomi sub-route of redirect (ii) is now
closed **with an in-repo citation** (the 2026-07-02 §4 single-arg refutation was
un-sourced at the time). What it **does not** do (per the STRICT "refuted"
discipline, scope (a) not (b)): it does not structurally exclude a
Plancherel-**fixed** E_q(2) vacuum row. That remains the one disciplined,
still-unbuilt form, and it still needs the Koornwinder–Swarttouw 1992 q-Hankel
kernel (paper ref [22]) — which `library/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials.pdf` cites but does not contain.

**Standing ask (unchanged from #3292):** to make the last disciplined q-Bessel
form testable, the specific source is **Koornwinder T.H., Swarttouw R.F., "On
q-analogues of the Fourier and Hankel transforms", Trans. AMS 333 (1992)** — its
q-Hankel transform + $J^{(3)}_\nu$ orthogonality measure fix the radial nodes.
Absent that, the honest resolution of the value step is redirect (iii): the
compact Verlinde/Hecke identity $S_{0\lambda}/S_{00} = d_q$
(`BWVacuumRowIsHecke`), near-definitional.
