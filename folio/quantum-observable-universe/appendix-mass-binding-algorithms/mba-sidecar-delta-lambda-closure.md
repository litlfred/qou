**Algorithm ($\Delta_\lambda$ per-partition value — PROVED; many-body magnitude — open).**
*Compute the per-partition binding weight $\Delta_\lambda(K)$
for an isotope knot $K$, consumed by Step 9b
([the per-isotope binding algorithm](#alg:per-isotope-binding)).*

### Input

- *Isotope knot $K$ + braid index $n_K$.*
- *Partition $\lambda \vdash n_K$.*

### Output

- *Per-partition weight $\Delta_\lambda = (-1)^{n(\lambda)}\dim V_\lambda \in \mathbb{Z}$
  (the signed Springer dimension; $n(\lambda)$ is the jet-order valuation
  parity, $\dim V_\lambda$ the Wedderburn dimension).*

  The name refers to the Springer correspondence: for a unipotent element $x$ of Jordan type $\lambda$ in $GL_n$, the top cohomology of the Springer fibre $\mathcal{B}_x$ is the irreducible $S_n$-module $V_\lambda$ \cite{springer1976}, \cite[Thm.~2.1]{shoji2019}. This explains the name only. The sign and the magnitude are derived independently below, and neither reference is an input to that proof.

### Status: value proved, magnitude external

**The per-partition value is PROVED, general-$n$:**
$\Delta_\lambda = (-1)^{n(\lambda)}\dim V_\lambda$
([the Donaldson–Thomas index unification proposition](#prop:delta-lambda-dt-index-unification);
value and chirality sign, with no $n \le 5$ restriction). The sign leg is the
jet-order valuation parity $(-1)^{n(\lambda)}$; the magnitude leg is
the Wedderburn dimension. Both are substrate-derived — not fitted.

**What remains open is NOT the value — it is the many-body binding MAGNITUDE.**
The six ansätze recorded below failed to derive the deuteron/light-nucleus
magnitude deficit $r^\ast \approx 1.585$, **not** the per-partition value. This is
a category distinction an earlier framing conflated:

- **Proved (value):** $\Delta_\lambda = (-1)^{n(\lambda)}\dim V_\lambda$.
- **Open (magnitude):** the additive **extensive** term. A per-block weight
  $\Delta_\lambda$ **cannot** supply it — the trace binding $B = E_0\,\Delta\mathrm{tr}_M$
  is intensive, and no per-block weight can convert an intensive quantity into an
  extensive one.
  The pairwise log-det cumulant is likewise **proved-capped at $A = 4$**:
  $\rho_4 \le C(4,2) = 6$, while strong targets need $\rho_4 \approx 13 > 6$,
  so the missing term is **super-pairwise** (irreducibly
  $\ge 3$-body). What is proved unconditionally is the single determinant
  inequality $(1-m^2)^6 \le (1+3m)(1-m)^3$ on $[0,1]$, which is the $A = 4$
  instance. The exclusion argument needs
  no more than that, since it is evaluated at the deuteron and $^4\mathrm{He}$; the
  general-$A$ bound $\rho_A \le C(A,2)$ remains unproved.

### Historical: the six refuted magnitude ansätze

These attempted to force the many-body magnitude into $\Delta_\lambda$; all were
refuted on the deuteron (each supplied the wrong $r^\ast$, none touched the now-proved value):

| Ansatz | Source | Refuted on |
|--------|--------|------------|
| Frobenius co-Casimir | early Frobenius-pairing proposals | deuteron |
| Demazure-fibre | symmetric-crystal early attempts | deuteron |
| LP-Plancherel | LP-based ansatz | deuteron |
| LP-Frobenius | LP-based ansatz | deuteron |
| crystal-graph naïve | KLR / Kashiwara level-0 | deuteron |
| augmented Markov | Markov-extension ansatz | deuteron |

### Correctness conditions

*[The binding-density remark](#rem:term6-binding-density)
fixes the binding sum's algebraic shape. The per-partition weight is now the
closed form $(-1)^{n(\lambda)}\dim V_\lambda$; the open piece is the separate,
super-pairwise extensive magnitude term (see Status).*

### Witness contract

*Per-partition $\Delta_\lambda$ values (the proved closed form) are emitted to
[`delta-lambda-witness.json`](../../../computations/delta-lambda-witness.json),
consumed by [`binding_K_direct.py`](../../../computations/binding_K_direct.py).
The witness carries the VALUE only — the binding total additionally requires the
$y_\lambda\,\chi^\lambda$ weighting and the separate extensive magnitude term
(open).*

### Notes

*The per-partition **value** is now proved; the **magnitude** is not, and six
fit-based ansätze have failed on it. A seventh fit would not advance the question:
under the three-calibration discipline a fitted magnitude is not a derivation. The
magnitude is a separate
additive extensive term (super-pairwise), and remains open.*
