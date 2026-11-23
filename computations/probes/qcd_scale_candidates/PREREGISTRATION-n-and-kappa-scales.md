# PREREGISTRATION — tower index n and KZ coupling κ as the scale of a colour coupling

Bean `qou-abzr` (GAP: no scale variable for a running coupling); sibling of `qou-bwwr`
(heat-kernel time t, scope-(a) miss, `computations/probes/qcd_heat_kernel/RESULT.md`).
Owner, 2026-11-22: *"try the tower index n or the KZ coupling κ as the scale instead of t"*.
Written and pushed **before** any probe code exists.

QCD reference, **comparison only, never input**: β₀ ∝ (11/3)C_A − (4/3)T_F n_f > 0
(antiscreening). No α_s or β₀ value enters anywhere; nothing is tuned to them.

**Forever gate.** κ ∼ log q is treated only as a running/family variable with q₀ a boundary
value. Nothing below solves for q₀ or selects q₀. The α_EM per-loop a₀ = 1/(4π) is not used and
not changed. No gluon is identified or selected (step 4 of def:derived-atom stays open).

## Common definitions (both arms)

- **Scale** s, oriented so that **s increasing = toward the IR**.
  N-arm: s = log n (more strands = coarser). κ-arm: s = log ℓ, ℓ = |z_i − z_j| (longer distance).
- **Channel weight** W_R(s) > 0 for a colour channel R of a fixed two-body colour decomposition.
- **Effective colour coupling** g²(s) := W_8(s) / W_1(s) (adjoint over singlet), the same
  definition as construction C1 of the heat-kernel probe, so the three scale candidates are comparable.
- **Running coefficient** b(s) := d log g² / ds. Discrete (N-arm):
  b(k) := log(g²(k+1)/g²(k)) / log(n_{k+1}/n_k); its **sign** is read exactly from g²(k+1)/g²(k) − 1.
- **Antiscreening** ⇔ b > 0 (coupling grows toward the IR). Screening ⇔ b < 0.
- **Log running (diagnostic, not part of the hit)**: 1/g²(s) contains a term linear in s with a
  nonzero coefficient as s → ∞ (the shape 1/g² = B·s + const of a one-loop β function).
  Power-law behaviour (b constant, or b → 0 as a power of 1/n) is recorded as "no log running".

## Hit rule (fixed now)

**HIT** iff (i) the sign of b is definite and does not change under any choice in the choice list
of that arm, **and** (ii) the leading coefficient splits into an identifiable C_A part and a T_F·n_f
part: the C_A part checked by its N-dependence (SU(N), N = 2, 3, 4 where computable: coefficient
∝ N), the T_F n_f part by its dependence on a count of fundamental strands/points that is not the
colour pair itself. **Otherwise MISS, scope (a)**: not found in the searched class. A miss excludes
nothing outside the class.

## N-arm — tower index n as a coarse-graining count

Setting: V = C³, U_q(gl₃), V^{⊗n} = ⊕_λ V_λ ⊗ S_λ (quantum Schur–Weyl, H_n(q) on S_λ),
n = 3k, singlet λ₁ = (k,k,k), adjoint λ₈ = (k+1,k,k−1). Adding three strands, k → k+1, is the
coarse-graining step (each step adds one colour-neutral baryon's worth of strands).

**N1 — Markov/Ocneanu isotypic weight (primary).** W_λ(n) := tr_q(P_λ) = f^λ · dim_q V_λ
(the U_q(gl₃) quantum trace of the λ-isotypic projector, i.e. the N = 3 Ocneanu trace up to the
common factor [3]_q^n, which cancels in g²). f^λ by the hook formula; dim_q by the q-Weyl formula.
For SU(N), N = 2, 3, 4: n = Nk, singlet (k^N), adjoint (k+1, k^{N−2}, k−1).
Choice list: q ↔ q⁻¹; the common normalisation of the trace (cancels); N.

**N2 — Jucys–Murphy branching weight.** W_λ(n) := average over standard tableaux T of shape λ of
the eigenvalue q^{2c_T(n)} of the last-strand Jucys–Murphy element L_n = σ_{n−1}⋯σ₁σ₁⋯σ_{n−1}
(c_T(n) = content of the box holding n), weighted by the branching f^{λ−□}/f^λ (Markov/Plancherel
branching H_{n−1} ⊂ H_n). This is the "add one strand" quantity named by the owner.
Choice list: q ↔ q⁻¹ (bar involution; the Hecke convention (σ−q)(σ+q⁻¹)=0 is symmetric under it up
to σ ↦ −σ⁻¹); the JM normalisation L_n vs q^{−1}L_n type scalings (cancel in the ratio only if
common to both channels).

**Predictions.**
- N1: g²(k) = (f^{λ₈}/f^{λ₁}) · [2]_q[4]_q (dim_q of the sl₃ adjoint). q enters only through the
  constant [2]_q[4]_q, so **b is q-independent and invariant under q ↔ q⁻¹**. The hook ratio
  f^{λ₈}/f^{λ₁} → N² − 1 as k → ∞ from below, with a 1/k correction whose coefficient I expect to
  be ∝ N (C_A-like, from a classical Casimir e^{−C/n} suppression). So I predict **b > 0
  (antiscreening direction), b = O(1/k) → 0, no log running, no n_f term** ⇒ MISS on clause (ii).
  The C_A identification of the 1/k coefficient is a prediction to be checked across N = 2, 3, 4.
- N2: the singlet's last box is always at content k − N (rectangle), the adjoint's at the three
  removable corners. g² is a Laurent polynomial in q with k-dependent rational weights. I predict
  **the sign of b is not invariant under q ↔ q⁻¹** ⇒ MISS on clause (i). No n_f term.

## κ-arm — KZ coupling κ, scale log |z_i − z_j|

Setting: ∇ = d − κ Σ_{i<j} Ω_ij d log(z_i − z_j) on W₁ ⊗ ⋯ ⊗ W_m, Ω = Σ_a t^a ⊗ t^a with
Tr_V(t^a t^b) = ½ δ^{ab} (Gell-Mann/2 for SU(3); the §48 normalisation, T·T = −C_F on the qq̄ singlet).
Drinfeld–Kohno: monodromy ↔ Jimbo R with q = e^{iπκ} (`kz-connection-sl2.md`, GLnResidues.lean).

Near a collision z_i → z_j the residue is κ Ω_ij; if no two eigenvalues of κΩ_ij differ by a nonzero
integer (non-resonance, `nonResonant_of_int_roots` in GLnResidues.lean) the solution is
z_ij^{κΩ_ij}·(holomorphic, invertible at 0), with no log terms. On the channel R ⊂ W_i ⊗ W_j the
exponent is κ ω_R, ω_R = (C_R − C_{W_i} − C_{W_j})/2.

**K1 (primary).** W_R(ℓ) := |z_ij^{κ ω_R}|², z_ij = ℓ e^{iθ}. g² = W_8/W_1, b = d log g²/d log ℓ.
Compute for: quark–antiquark (3 ⊗ 3̄ = 1 ⊕ 8), gluon–gluon (8 ⊗ 8 ∋ 1, 8), and for SU(N),
N = 2, 3, 4 (N ⊗ N̄). Eigenvalues computed from explicit matrices (sympy), checked against the
Casimir formula.
Choice list: κ real (|q| = 1) vs κ imaginary (q real > 1, the qou case: κ = −i log q₀/π);
sign of κ; normalisation of Ω (rescales κ); a scalar framing shift Ω → Ω + c (cancels in g²).

**K2 — log terms.** Resonance condition κ(ω_R − ω_R') ∈ Z∖{0} for the channels present; translate
to q = e^{iπκ}. Log ℓ terms (the only source of logarithmic running in a Fuchsian system) appear
only at resonance.

**K3 — n_f dependence.** Add fundamental points (quarks) at other positions; check whether the
leading collision exponent of the colour pair changes (prediction: no; spectators enter only at
O(z_ij)).

**Predictions.**
- K1: ω_8 − ω_1 = C_A/2 for **every** external representation (since C_1 = 0, C_8 = C_A), so
  b = κ·C_A (κ real) — quark pair and gluon pair give the **same** b: **no quark/gluon separation**.
  Sign of b = sign of κ ⇒ choice-dependent ⇒ MISS on clause (i). For κ imaginary (qou's real q₀):
  |z^{κω}| depends on θ only, **b = 0 exactly** in log ℓ (the scale dependence is a pure phase;
  the θ-dependence is monodromy). Power law, never log.
- K2: for 3 ⊗ 3̄, resonance ⇔ 3κ/2 ∈ Z∖{0} ⇔ q a root of unity; **never at real q > 1**.
  So at qou's q₀ no log running arises at any two-point collision.
- K3: no n_f in the leading exponent ⇒ no T_F n_f term ⇒ MISS on clause (ii).
- Overall predicted verdict: **MISS on both arms, scope (a).** C_A does appear, but as a Casimir
  difference (tree-level one-gluon exchange), not as a loop coefficient, and without a T_F n_f partner.

## Honesty clause

Every construction above is reported whatever it gives, including any prediction that fails.
Post-hoc checks are labelled post-hoc. No construction is added or dropped after seeing numbers
without saying so. No comparison value is used as input. A miss is reported as scope (a); no
structural exclusion is claimed without a proved invariant. Exact sympy only; mpmath only for a
read-out at the proton pin; no float64.
