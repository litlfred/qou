# Descent involution τ̂₀ — proton-scale numerical realisation

**Date**: 2026-05-03
**Phase**: A.3 of issue #522 (mass-tower level-1 computation)
**Verdict (initial)**: `setup-only` — stub artifact committed; computation in progress.

## Goal

Build a concrete numerical realisation of the descent involution
$\hat{\tau}_0 = \ell_0 \circ \mathfrak{d}_1$ acting on $\mathrm{End}_{\mathbf{C}}(A_1)$ at the proton scale ($A=1$).

Verify:

1. $\hat{\tau}_0^2 = \hat{\tau}_0$ (idempotence) to f64 floor.
2. Decompose $\mathrm{End}_{\mathbf{C}}(A_1) = \mathrm{im}(\hat{\tau}_0) \oplus \ker(\hat{\tau}_0)$ (descended ⊕ transient).
3. Report dim(descended), dim(transient).

## Definitions (cited)

- **A_0 = H_3(q₀)** — concrete rank-3 Iwahori–Hecke algebra at substrate value $q_0 \approx 1.1097$. Specht decomposition: $1 + 2 + 2 + 1 = 6$ (trivial + 2-copies of standard + sign), so $\dim_{\mathbb{C}} A_0 = 6$.
- **Ω¹(A_0) = ker(m: A_0 ⊗ A_0 → A_0)** — Kähler differentials (universal first-order calculus). Expected dim = 36 − 6 = **30**.
- **A_1 = J^1(A_0) = A_0 ⊗ Ω^1(A_0)** — expected dim = 6 × 30 = **180**.
- **ℓ_0: A_0 ↪ A_1** — ascent embedding.
  - From `descent-lemma-proof.md` Step 1: the unit section is
    $\eta \otimes \mathrm{id}\colon \Omega^1(A) \hookrightarrow A \otimes \Omega^1(A)$.
  - For our purposes (need $A_0 \to A_1$, not $\Omega^1 \to A_1$), we
    use the canonical splitting $a \mapsto a \otimes d(1)$ where
    $d \colon A \to \Omega^1(A)$ is the universal derivation. Since
    $d(1) = 0$ in the unital Kähler differential, we instead use the
    standard inclusion $A \to A \otimes A \to A \otimes \Omega^1$
    via $a \mapsto a \otimes (1 \otimes 1 - 1 \otimes 1) + \cdots$;
    see § Choice of ℓ_0 below.
- **𝔡_1: End(A_1) → End(A_0)** — descent homomorphism. From
  `descent-lemma-proof.md` Step 1, the underlying object map is
  $r_1 = \varepsilon \otimes \mathrm{id} \colon J^1(A) \to A$
  (counit on the first factor). The induced descent on endomorphisms
  is conjugation: $\mathfrak{d}_1(\phi) = r_1 \circ \phi \circ \ell_0$.
- **τ̂_0 = ℓ_0 ∘ 𝔡_1**: the projector $\mathrm{End}(A_1) \to \mathrm{End}(A_1)$,
  whose image is $\ell_0 \mathrm{End}(A_0) r_1$ (descended endomorphisms).

## Key construction notes

The narrative in `descent-lemma-proof.md` describes ℓ_0 / r_1 acting on the
**Frobenius-Hopf object** $A$. For the Hecke algebra realisation $A_0 = H_3(q_0)$,
we read these as $\mathbb{C}$-linear maps using:

- $\eta \colon \mathbb{C} \to A_0$, $1 \mapsto e$ (identity element).
- $\varepsilon \colon A_0 \to \mathbb{C}$, the augmentation: $\varepsilon(a) = $
  trace projection onto trivial Specht block (Markov-like).

So:
- $\ell_0 \colon A_0 \to A_0 \otimes \Omega^1$, $a \mapsto a \otimes \omega_0$
  for a fixed unit vector $\omega_0 \in \Omega^1$ representing
  $d(\text{generator}) \neq 0$.
- $r_1 \colon A_0 \otimes \Omega^1 \to A_0$, $a \otimes \omega \mapsto \varepsilon(\omega) \cdot a$.

Then $\mathfrak{d}_1 \circ \ell_0 = \mathrm{id}_{A_0}$ iff
$\varepsilon(\omega_0) = 1$ — but $\omega_0 \in \ker(m)$ does **not**
factor through $\varepsilon$ in general. **This is a math gap** to flag:
the proof reads as object-level Frobenius restriction, not as a unit-counit
splitting compatible with $\Omega^1 = \ker(m)$.

## Choice of ℓ_0 — the canonical retraction-of-Kähler-differential

Standard non-commutative geometry (Connes, Loday) gives the universal
short exact sequence:

$$
  0 \to \Omega^1(A) \to A \otimes A \xrightarrow{m} A \to 0,
$$

split (as a left-A module) by $s\colon A \to A \otimes A$, $a \mapsto a \otimes 1$.
Then $A \otimes A \cong A \oplus \Omega^1$ via $s + (1 - s \circ m)$.

The canonical ascent that realises Step 1 of `descent-lemma-proof.md` is

$$
  \ell_0 \colon A \to A \otimes \Omega^1(A), \quad
  a \mapsto a \otimes (1 \otimes 1 - s(m(1 \otimes 1))) = 0.
$$

This vanishes — confirming that Ω^1 has no canonical "unit element". The
descent retraction is then the multiplication on the second factor:

$$
  r_1 \colon A \otimes \Omega^1 \hookrightarrow A \otimes A \otimes A
  \xrightarrow{\mathrm{id} \otimes m} A \otimes A \xrightarrow{m} A.
$$

This is the **canonical retraction of the Kähler differential** in non-commutative geometry. With this choice:

- $\ell_0$ is **not** uniquely defined without additional data
  (e.g., a flat connection).
- The pair (ℓ_0, 𝔡_1) requires a chosen connection $\nabla \colon A \to \Omega^1$,
  which is part of the data of the brane tower.

**Math gap**: the content blocks `descent-involution.md` and
`descent-lemma-proof.md` describe ℓ_0 / 𝔡_1 abstractly. The numerical
realisation requires picking a concrete connection $\nabla$. We use the
**trivial connection** $\nabla(a) = a \otimes 1 - 1 \otimes a$ embedded
into $\Omega^1$.

## Inventory of existing infrastructure

| Module | Role |
|---|---|
| `folio-assistant/computations/hecke_core.py` (3155 lines) | YSN matrices for partitions; not a clean H_3 multiplication table. |
| `folio-assistant/computations/hecke_symbolic.py` (905 lines) | Symbolic Hecke division (Gröbner-style). Does not give regular rep directly. |
| `folio-assistant/computations/schur_weyl_q_hecke_v2.py` (294 lines) | Schur–Weyl q-Hecke, partition-indexed, not regular rep. |
| `folio-assistant/computations/kahler_lift.py` (343 lines) | **Misleading name** — this is the Hoefsmit/Markov q-derivative lift, *not* the universal Kähler differential. |
| `folio-assistant/computations/jet_lifted_hecke.py` (302 lines) | Jet lift via aggregated character traces; not the J^1 = A ⊗ Ω^1 functor. |
| `q_parameter.py` | Source of truth: `q₀ = 1 / (1 − √(Vol(4_1)/(m_μ/m_e)))`. |

**Conclusion**: there is **no existing module** that builds Ω^1 as
ker(m) explicitly, nor that materialises End(A_1) numerically. This
realisation is new infrastructure.

## Plan

1. **Step 1 (built)**: stub witness committed. ✓
2. **Step 2**: build H_3(q) as 6-dim algebra via direct Specht block
   matrices ($1 \oplus 2 \oplus 2 \oplus 1$).
3. **Step 3**: form m: A_0 ⊗ A_0 → A_0 as a 6 × 36 matrix; SVD ker.
4. **Step 4**: Ω^1 basis (30-dim).
5. **Step 5**: A_1 = 180-dim; ℓ_0 (with chosen trivial connection),
   r_1 (canonical retraction).
6. **Step 6**: build a small principal sub-block of End(A_1)
   (probably ℓ_0 End(A_0) r_1 + a transient transversal); verify
   idempotence.
7. **Step 7**: report dimensions; finalise verdict.

## Conjectural propagation note

Per CLAUDE.md §3b: this audit memo describes a **numerical witness**,
not a logical claim. No conjectural propagation issues.

## Files

- Witness JSON: `folio-assistant/computations/tau-hat-n-proton-realisation.witness.json`
- This memo: `docs/audits/2026-05-03-tau-hat-n-proton-realisation.md`
- (Forthcoming) script: `folio-assistant/computations/tau_hat_n_proton_realisation.py`
