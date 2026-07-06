# Level-1+ jet contributions for ALL binding-energy terms — structural probe

## Setup

The level-0 hybrid models FREE nucleon mass
([4He deep dive](2026-05-02-4He-spread-deep-dive.md)). To close
the cal/m_e spread, level-1+ jet contributions must capture all
five SEMF (semi-empirical mass formula) terms plus shell
corrections. This memo probes each term's QOU-categorical
candidate mechanism.

**SEMF reference** (Bethe–Weizsäcker, 1935–1936):

$$
B(Z, A) = a_V A - a_S A^{2/3} - a_C \frac{Z(Z-1)}{A^{1/3}} - a_A \frac{(N-Z)^2}{A} + a_P \frac{(-1)^Z + (-1)^N}{2 A^{1/2}}
$$

with empirical coefficients (MeV):
$a_V \approx 15.75$, $a_S \approx 17.80$, $a_C \approx 0.711$,
$a_A \approx 23.69$, $a_P \approx 11.18$.

Shell corrections: discontinuities $\sim 1$–$2$ MeV at $Z, N \in
\mathfrak{M} = \{2, 8, 20, 28, 50, 82, 126\}$.

---

## Term 1 — Volume ($a_V \cdot A$, ~15.75 MeV/nucleon)

**SEMF role.** Bulk binding from short-range strong interaction;
nucleons in the interior bond with all neighbors.

**QOU candidate.** Already partially encoded in level-0:
`single = A · Φ_q(|tr_nucleon|)`. But Φ_q(0.671) = 1850
*Hecke-units* gives the FREE nucleon mass; the binding is the
**deviation** of the actual per-nucleon mass from the free
prediction.

**Level-1 mechanism.** Per-nucleon **descended-trace
correction**. The level-1 single-nucleon contribution is

$$
\Phi_q(|tr_M^{(1)}(\xi)|)
$$

where $\xi$ is the jet-prolonged single-nucleon braid on
$A_1 = A_0 \otimes \Omega^1(A_0)$. The Kähler differential
$\Omega^1$ supplies the binding-correction kernel. Per
`prop:per-braid-mass-tower`'s jet form, this is the level-1
piece of $\sum_{\xi \in \mathcal{S}_1^{(n)}}$.

**Scaling.** Linear in $A$ by construction (per-nucleon sum).
Constant per-nucleon correction → matches $a_V \cdot A$.

**Status.** Implementation requires the explicit jet-prolonged
trace formula. Closest existing infra: `multi_level_jet_sum.py`
(stub) + `jet_lifted_hecke.py` (Markov-stabilization or
q-Plancherel-descent lifts). Volume coefficient $a_V$ would be
the structurally-determined deviation of $\Phi_q^{(1)}$ from
$\Phi_q^{(0)}$.

---

## Term 2 — Surface ($-a_S \cdot A^{2/3}$, ~17.80 MeV)

**SEMF role.** Surface nucleons have fewer neighbors than
interior ones; reduces binding by a factor proportional to
surface area.

**QOU candidate.** The braid's **boundary structure** — strands
with fewer crossings. In a 3A-strand atomic braid, "interior"
strands have $\sim A$ partners; "surface" strands have fewer.

**Level-1 mechanism.** Boundary-stratum correction. Per
`def:algebraic-quantum-volume`, the volume specialization
distinguishes inner from outer crossings. The level-1
contribution from BOUNDARY sub-braids (those with truncated
partner sets) gives a correction scaling as the surface count.

**Scaling.** $A^{2/3}$ comes from the geometric ratio
$\text{surface} / \text{volume} \propto r^2 / r^3 = 1/r \propto
A^{-1/3}$, so surface $\propto A \cdot A^{-1/3} = A^{2/3}$.
Algebraically: the count of "incomplete pair partners" scales
as the boundary of a 3D nucleon arrangement, $A^{2/3}$.

**Status.** Not currently implemented. Would require a notion
of "boundary strand" in the atomic braid — analogous to the
Lüders-Wenzl skein theory's boundary handling. PR #500's
`optimised_magic_verifier` may be relevant via the LR-fusion
shell-pair $(i_Z, i_N)$ structure (boundary = highest occupied
shell, which is partially filled at $A < $ next magic).

---

## Term 3 — Coulomb ($-a_C \cdot Z(Z-1)/A^{1/3}$, ~0.71 MeV/pair-density)

**SEMF role.** Electrostatic repulsion between proton pairs;
scales as $Z(Z-1) / r$ where $r \propto A^{1/3}$.

**QOU candidate.** The pair tower in the level-0 hybrid HAS
proton-proton, proton-neutron, neutron-neutron pair contributions
separately:

$$
z^2 \cdot [n_{pp} \cdot \Phi_q(|tr_{pp}|) + n_{nn} \cdot \Phi_q(|tr_{nn}|) + n_{pn} \cdot \Phi_q(|tr_{pn}|)]
$$

But at q=1 MN: $|tr_{pp}| = |tr_{pn}| = |tr_{nn}| = 0.0156$.
Identical. The Coulomb-distinguishing structure is **invisible
at q=1 MN**.

**Level-1 mechanism.** **q-Hecke per-pair distinction**. The
descended q-Hecke trace at A=3 splits ³He vs ³H by 0.53 MeV
(matching AME) — that's the q-Hecke isospin distinguishing
working. At pair level, q-Hecke gives:
- $|tr_{pp}^{(\text{q-Hecke})}| = 0.823$
- $|tr_{nn}^{(\text{q-Hecke})}| = 0.601$

with 27% relative difference (per
[2026-05-01-q-hecke-norm-analysis](2026-05-01-q-hecke-norm-analysis.md)).
Computing $\Phi_q$ on these q-Hecke pair traces gives
proton-proton Coulomb-like enhancement.

**Scaling.** $Z(Z-1)/2$ pp pairs in the cross sum, weighted by
$\Phi_q(|tr_{pp}^{(\text{q-Hecke})}|)$ different from
$\Phi_q(|tr_{pn}^{(\text{q-Hecke})}|)$. Need an additional
$1/A^{1/3}$ factor — comes from the brane-tower volume scaling
(braid length grows as $3A$, but the relevant geometric scale
is the brane $A^{1/3}$).

**Status.** **Tractable.** Replace the q=1 MN per-pair traces in
the cross tower with the q-Hecke per-pair traces. This is a
direct extension of `markov_trace_q_hecke_atomic` from descended
to pair level.

---

## Term 4 — Asymmetry ($-a_A \cdot (N-Z)^2/A$, ~23.69 MeV)

**SEMF role.** Penalty for proton-neutron imbalance;
$\propto (N-Z)^2/A$ from the Pauli exclusion / shell-filling
structure (excess of one type sits in higher levels).

**QOU candidate.** **Pair-of-pairs correlations** at level 1.
The $S_4^{(n)}$ stratum (4-element subsets) at level $n=1$ gives
contributions from quadruples of nucleons. At level 0 these
appear in the all-pairs sum as $\binom{A}{2}$ pairs; at level 1
they appear as $\binom{A}{4}$ pair-of-pairs (or 4-cycle
contributions in the Wedderburn block decomposition).

**Mechanism.** The Wigner energy formula
([prop:wigner-np-pairing](../../content/quantum-observable-universe/braids-and-knots/wigner-np-pairing.md))
already gives a pair-pair contribution. Extending to the
level-1 jet would yield $(N-Z)^2/A$ structure naturally:
$(N-Z)^2$ counts the number of "unbalanced" pair-of-pairs (those
that can't form symmetric singlets).

**Scaling.** Quadratic in $|N - Z|$, with $1/A$ damping from
the categorical-trace normalization. Matches SEMF.

**Status.** Partial — `prop:wigner-np-pairing` provides the
algebraic structure. Need to wire a level-1 evaluator that uses
$(N-Z)^2$-weighted pair-of-pairs.

---

## Term 5 — Pairing ($\pm a_P / A^{1/2}$, ~11.18 MeV)

**SEMF role.** Like-nucleon pair binding bonus (even-even
strongly bound, odd-odd weakly bound, odd-A intermediate).

**QOU candidate.** **Parity-of-A structure** in the
self-conjugate partition sum. Self-conjugate partitions of
$n = 3A$ split by parity; their contribution sums depend on
$(-1)^A$ in a structurally explicit way.

**Mechanism.** From the Murnaghan-Nakayama character on
even-vs-odd cycle-type permutations, plus the BB-stratum
parity grading. The level-1 contribution from
$\mathbb{Z}/2$-graded BB strata:

$$
m^{(1)}_{\text{pairing}}(Z, N) = \frac{(-1)^Z + (-1)^N}{2} \cdot \sum_{\lambda \text{ self-conj}} \delta_{|\lambda| \text{ even/odd}} w_\lambda^{(1)}
$$

The $1/A^{1/2}$ scaling comes from $1/\sqrt{[3A]_q}$ in the
q-Plancherel measure normalization.

**Status.** Conjectural-level. The parity grading on
self-conjugate $\lambda$ is computable
([enumerate_self_conjugate_partitions.py](../../computations/enumerate_self_conjugate_partitions.py)
already enumerates them); the parity classification of each
partition's "shape" is the missing piece.

---

## Shell corrections (discontinuities at magic Z, N)

**Phenomenology.** Binding-curve drops abruptly at
$Z, N \in \mathfrak{M}$ — extra $\sim 1$–$2$ MeV per nucleon
below the SEMF prediction.

**QOU candidate.** **Categorical-neutrality saturation** per
`conj:categorical-neutrality-saturated-shells`: at saturated $n$
the $\Phi_n$ is supported only on self-conjugate $\lambda \vdash
n$, content sum zero. The full-twist $\Delta_n^2$ acts trivially.

**Mechanism.** The level-1 contribution from $\lambda$ with
$c(\lambda) = 0$ (self-conjugate) ENRICHES at magic shells;
at non-magic, the $c(\lambda) \neq 0$ partitions also enter
but with a non-trivial full-twist phase $q^{c(\lambda)}$ that
modifies the contribution.

The DIFFERENCE between magic and non-magic at level 1 is the
"shell correction" — algebraically:

$$
\Delta_{\text{shell}}^{(1)}(n) = \sum_{\lambda \text{ self-conj}} w_\lambda^{(1)} \cdot \chi^\lambda(\beta) \cdot \begin{cases} 1 & n \in \mathfrak{M} \\ q^{c(\lambda)} & n \notin \mathfrak{M} \end{cases}
$$

The $q^{c(\lambda)}$ phase at non-magic kills the contribution
on average (cancellations); at magic the phases are 1 and the
sum survives.

**Status.** Hardest piece. Requires the explicit level-1 weight
$w_\lambda^{(1)}$, the self-conjugate $\lambda$ enumeration
(have), and the BB-spectral-sequence collapse condition
([conj:homological-shell-condensation](../../content/quantum-observable-universe/lifting-and-descent/homological-shell-condensation.md)).

---

## Summary table

| SEMF term | Empirical (MeV) | QOU level | Mechanism | Tractability |
|-----------|----------------:|:---------:|-----------|:------------:|
| Volume | $15.75 \cdot A$ | 1 | Per-nucleon descended-trace correction | medium |
| Surface | $-17.80 \cdot A^{2/3}$ | 1 | Boundary-stratum correction | hard |
| Coulomb | $-0.71 \cdot Z(Z-1)/A^{1/3}$ | 0+ | q-Hecke per-pair (extends descended path) | **easy** |
| Asymmetry | $-23.69 \cdot (N-Z)^2/A$ | 1 | Pair-of-pairs Wigner extension | medium |
| Pairing | $\pm 11.18 / A^{1/2}$ | 1 | Parity-graded self-conjugate λ sum | medium |
| Shell | $\pm 1$–$2$ at magic | 1 | BB-saturated self-conj λ enrichment | hard |

## What's tractable now

**Coulomb term (Term 3) is the immediate win.** The level-0 cross
tower already iterates pp/pn/nn pairs separately, but at q=1 MN
the traces are identical. Switching the cross tower to use
q-Hecke per-pair traces (already computed in
`schur_weyl_q_hecke_v2`) gives the proton-proton Coulomb-like
enhancement automatically.

**Estimated impact**: the Coulomb correction at 4He is small
(~0.71 MeV / 1 = 0.71 MeV bare, but $Z(Z-1)/A^{1/3}$ at 4He
gives 0.45 MeV total). At 16O and 40Ca, Coulomb contributes
~14.4 and ~73.4 MeV respectively — significant. This term alone
should noticeably improve cal/m_e at heavy atoms.

**Combining Coulomb with the existing level-0 hybrid** is a
1–2 day implementation. It won't close the spread to 22 ppb
(other terms still missing) but it's the cheapest meaningful
step toward bound-mass prediction.

## Recommendation

1. **Immediate (1–2d)**: implement Coulomb-correction (Term 3)
   by replacing q=1 MN per-pair traces with q-Hecke per-pair
   traces in `per_braid_tower_hybrid.py`. Test cal/m_e change.
2. **Short-term (1w)**: probe Asymmetry and Pairing via existing
   `prop:wigner-np-pairing` machinery; estimate magnitude.
3. **Medium-term (2–4w)**: derive level-1 weight $w_\lambda^{(1)}$
   from BB-spectral-sequence; implement Volume + Shell.
4. **Long-term**: Surface — requires categorical formulation of
   "boundary strand" not currently in the framework.

Steps 1–2 should drop the cal/m_e spread substantially without
the heavy A.3 v3 work. Steps 3–4 close to ~22 ppb.
