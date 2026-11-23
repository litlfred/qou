# Pre-registration: the ruled flavour split ε on the siblings' four-strand hydrogen element (2026-11-22)

Owner, 2026-11-22: use the sibling work (PR #8804 §46; branch `claude/hydrogen-capture-lean-2026-11-22`)
and see what it implies. Written before `np_hydrogen_flavour_split_probe.py` is run.

## Honesty clause (read first)
Before writing this I computed one combination by hand, and I am recording it so the numbers below
cannot be read as a blind test. It is E₀^full·(ε(V³) + |S_B1|) = 0.78189 MeV, where ε(V³) = t_p − t_n
on three strands (the ruled Q_β cell, 0.3254 MeV) and S_B1 = h²[3]_q/q² is the sibling's capture
asymmetry (0.4565 MeV). CODATA Q_β is 0.78233 MeV, so this is −0.057 %. The sum adds two **different**
functionals:
- ε is the K-weighted normalised quantum trace;
- S is the sibling's T³-weighted B1 functional.

It also takes the placement whose sign makes them add. That is selection against the target, and it
is **not** adopted. This probe asks the question that would make it legitimate: what does **one**
functional, the ruled one, give on the full hydrogen element?

## Setup (fixed)
- Ř as in the §42–§46 engine: [[q,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,q]], h = q − q⁻¹. Exact sympy
  over Q(q).
- Ruled functional, unchanged from the Q_β cell: E_c(W) = Tr(K^{⊗4}·Π_c·W)/[2]⁴, K = diag(q, q⁻¹),
  u = index 0. Π_c restricts the three proton strands to weight (2,1) (p) or (1,2) (n). The electron
  strand is traced, not restricted.
- ε(W) = E_p(W) − E_n(W).
- Control: the three-strand computation reproduces t_p = −P/(q²(q²+1)³) and t_n/t_p = q⁻². Checked
  before registering.
- Elements (from the sibling pre-registration, unchanged):
  - **W0** V³ on proton strands 0–2, electron strand 3, no capture.
  - **W_L** = V³·(σ₂σ₁σ₀σ₀σ₁σ₂)⁻¹, the cabled capture, proton left.
  - **W_R**, the mirror: proton strands 1–3, V = σ₂σ₁⁻¹, capture (σ₀σ₁σ₂σ₂σ₁σ₀)⁻¹.
  - **W_adj,L / W_adj,R**, the adjacent capture σ₂⁻² (resp. σ₀⁻²).

## Predictions
- **H1.** ε(W0) = ε(V³) on three strands, since the electron strand factor is tr(K)/[2] = 1.
- **H2.** ε(W_L) and ε(W_R) are reported exactly. No prediction is made for their sign or size.
- **H3.** The ratio t_n/t_p on W_L is not q⁻² (the capture couples the electron's weight to the quark
  strands). This is a guess, stated in advance.
- **H4.** Whatever the result, it is not compared for selection. E₀^full·|ε| is printed next to
  CODATA only as a comparison, and the two placements are both reported.
