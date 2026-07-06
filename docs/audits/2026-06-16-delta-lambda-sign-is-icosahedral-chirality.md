# Deuteron Δ_λ closure = (Wedderburn magnitude) × (icosahedral chirality sign)

**Date:** 2026-06-16
**Branch:** `claude/option-e-delta-lambda-sign-chirality-2026-06-16`
**Status:** structural result connecting the Δ_λ closure (Option-E) to the s5-so3 keystone; verified, no fit.
**Discipline:** formalize-first.

> **⚠ Correction (2026-06-16, post-merge).** The word "closed" in the title/§Statement is **wrong** and is
> retracted. Running the canonical compute (`computations/binding_energy_categorical_deuteron.py`) shows the
> per-λ **sum** `Σ_λ y_λ χ^λ(β_D) Δ_λ` with `Δ_λ = sgn·dim` gives `B(D)=0.380 MeV`, **−82.9 %** off AME — it does
> **not** close the deuteron. The deuteron binding is closed separately by **`E₀×q⁻¹` (+0.91 %)**,
> `E₀=m_e/(q₀(q₀−1))` (PR #1367). **What stands:** `Δ_λ=sgn·dim` is the *proved categorical per-block factor*
> (PR #1305), and its **magnitude×chirality decomposition** + the explanation of the PROBE-4 positivity prune are
> unaffected — they are statements about the Δ_λ *factor*, not a closure of the binding energy. Full cross-check:
> [`2026-06-16-deuteron-closure-crosscheck-and-correction.md`](2026-06-16-deuteron-closure-crosscheck-and-correction.md).
> Read "Δ_λ closure" below as "Δ_λ *structural factor*".

## Statement

`Δ_λ = sgn(w₀^{S_λ'})·dim(V_λ)` is the proved categorical **per-block factor** of the binding formula (it does
**not** by itself close the deuteron — see the correction banner above). This note makes the reading
**"magnitude = Wedderburn, sign = chirality"** precise and ties it to the merged
s5-so3 keystone (where the icosahedral chirality is the $S_5\setminus A_5$ parity swapping $T_1\leftrightarrow T_2$).

## Magnitude = Wedderburn (chirality-invariant)

$|\Delta_\lambda| = \dim(V_\lambda)$ is the dimension of the $\lambda$ **Wedderburn block** of $H_n(q)$ at generic
$q$ (the Specht / Hoefsmit module). It is **chirality-invariant**: the transpose preserves dimension,
$\dim(V_\lambda)=\dim(V_{\lambda'})$ (verified for all $\lambda\vdash1..6$). So flipping chirality cannot change
the magnitude — only the sign.

## Sign = chirality (the transpose / sign-character twist)

$\mathrm{sgn}(w_0^{S_{\lambda'}})$ is a function **purely of the transpose** $\lambda'$ (the column lengths). The
transpose involution $\lambda\leftrightarrow\lambda'$ **is** the sign-character twist of $S_n$:
$$V_\lambda\otimes\mathrm{sgn}\;\cong\;V_{\lambda'}.$$
On the keystone side ($A_5\subset S_5$) the sign character is the $S_5\setminus A_5$ **parity** — exactly the
operation that swaps the icosahedral chiral pair $T_1\leftrightarrow T_2$ (merged keystone result; an odd
permutation fuses the two $A_5$-classes of 5-cycles and exchanges $T_1,T_2$). Therefore the Δ_λ **sign is the
icosahedral chirality**, evaluated on the column data of $\lambda$.

**Chirality-fixed ⟺ A₅-split.** The self-conjugate partitions ($\lambda=\lambda'$) are the chirality-fixed points
of the transpose involution. Among partitions of 5 the **unique** self-conjugate is $(3,1,1)$ (verified) —
exactly the block whose $A_5$-restriction **splits** into the chiral pair $T_1\oplus T_2$ (the electron/tau
block, merged keystone result). So "chirality-fixed under the sign-twist" and "$A_5$-restriction splits into the
icosahedral chiral pair" are the **same** condition. This is the precise bridge: the Δ_λ closure's sign and the
keystone's $T_1/T_2$ chirality are one structure.

(Verified: `scripts/option_e_delta_lambda_sign_chirality.py`, exit 0.)

## Why this matters for Option-E

- It explains, structurally, **why the PROBE-4 KL-positivity prune holds**: the Δ_λ sign is the chirality
  (a $\pm1$ from the sign-character twist), and KL/crystal multiplicities are non-negative — they live on the
  *magnitude* side, never the sign. Magnitude = Wedderburn (where positive KL data could in principle contribute
  $\dim$); sign = chirality (exogenous, geometric). The merged prune and this decomposition are the same fact
  seen from two sides.
- It gives the A=4 frontier (**PROBE 2**, sibling cluster #2369/#2371/#2372) a structural template: the
  interface operator should supply the per-block **magnitude** (Wedderburn / quantum-dimension data), with the
  **sign** factored as the chirality $\mathrm{sgn}(w_0^{S_{\lambda'}})$ — *not* sought inside the operator's
  (positive) structure.

## Net

No new closure and no fit — a structural identification: the closed deuteron Δ_λ factorises as
**Wedderburn magnitude × icosahedral-chirality sign**, unifying the Option-E Δ_λ closure with the s5-so3
keystone's chirality. The A≥4 extension remains PROBE 2 (sibling-owned).

## Cross-references

- `docs/audits/2026-05-26-delta-lambda-binding-formula-closure.md` — the deuteron `sgn·dim` closure
- `docs/audits/2026-06-16-option-e-probe4-kl-positivity-prune.md` + `...-kl-engine-verified.md` — the positivity prune (sign exogenous)
- `docs/coordination/s5-so3-keystone.md` — chirality = $T_1/T_2$ under $S_5\setminus A_5$
- `scripts/option_e_delta_lambda_sign_chirality.py` — this verification (exit 0)
