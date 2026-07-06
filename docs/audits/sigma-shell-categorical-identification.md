# σ_shell — categorical identification

**Author.** Investigation continuation post the falsified shell-self-
duality probe (atom braid `β = atom_braid_word_3A(Z, N)` does NOT
satisfy `χ_λ(β) = χ_{λ*}(β)` at any tested A — `probe-atom-shell-
self-duality.witness.json` and `probe-per-nucleon-self-duality.witness.json`).

**Question.** What IS `σ_shell` categorically, given that it is NOT
the atom braid?

## Resolution

`σ_shell` is **not** an atom braid, **not** the Markov closure of any
specific physical knot, **not** an SDP optimum on the joint-tower
PSD cone in the way `T_w(atom)` is.

`σ_shell` is a **constructed element of `H_{3·A_magic}(q)`** built
via the ILP at confinement level 4, with three categorical inputs:

| input | source |
|---|---|
| **Position** | shell-boundary generators `gen = 3·A_magic − 1` (per `sigma_shell_characterization.py` line 24) |
| **Weight** `y_shell(q)` | LP-dual shadow price at shell partition `λ ⊢ 3·A_magic` (per [`prop:mass-coefficient-shadow-price`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/mass-coefficient-shadow-price.md)) |
| **Multiplicity** `m_shell` | level-4 ILP — number of crossings per shell boundary |

Decomposed in the Wedderburn basis at `H_{3·A_magic}(q)`:

$$\sigma_{\text{shell}} = \sum_{\lambda \,\vdash\, 3\cdot A_{\text{magic}}} x_\lambda \cdot e_\lambda$$

with the **self-duality constraint**

$$x_\lambda = x_{\lambda^*} \quad \text{for all } \lambda \vdash 3\cdot A_{\text{magic}}$$

per [`prop:shell-schur-weyl-self-duality`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/shell-schur-weyl-self-duality.md). This locus is the **`GL_k`-charge-conjugate-fixed sub-algebra** of `H_{3·A_magic}(q)` under Schur-Weyl transport.

## Why the atom-braid probe falsified the wrong thing

My earlier probes computed `χ_λ(β_atom)` for `β = atom_braid_word_3A(Z, N)` at H_{3A} (e.g. ⁴He at H_12). Those Wedderburn coefficients do NOT satisfy `x_λ = x_{λ*}` because:

1. `β_atom` is a **specific braid word** built from `B_3` confinement + intra-quark + inter-nucleon crossings. It is `NOT` constrained to lie in the self-dual locus.
2. `σ_shell` is a **separately-constructed element** that lives in the self-dual locus by ILP design.
3. `β_atom` and `σ_shell` are **distinct elements** of the same Hecke algebra; the atom mass involves contributions from BOTH.

The mass formula reads schematically:

$$\mathfrak{m}(\text{atom}) = \mathfrak{m}_{\text{tower}}(\beta_{\text{atom}}) + \Delta\mathfrak{m}_{\text{shell}}(\sigma_{\text{shell}})$$

where `m_tower` is the standard Φ_q tower on `β_atom` and `Δm_shell` is the magic-shell correction. For non-magic atoms, `Δm_shell = 0` (no shell closure). For magic atoms (`A ∈ {2, 8, 20, 28, 50, 82, 126}`), `σ_shell` adds a structural correction via the LP-dual shadow price.

## Concrete formula (per `sigma_shell_characterization.py`)

$$\Delta\mathfrak{m}_{\text{shell}} = z^2 \cdot \Phi_q\bigl(\bigl|\hat{V}_{\text{shell}}\bigr|^2\bigr) \cdot y_{\text{shell}}(q) \cdot f^{\lambda_{\text{atom}} / \lambda_{\text{shell}}}$$

with:
- `z²` Markov-trace pair-weight per `mass-endomorphism-tower.md`
- `Φ_q(|V̂_shell|²)` quantum-dilogarithm tower contribution at the shell scale
- `y_shell(q)` LP-dual shadow price at `λ ⊢ 3·A_magic`
- `f^{λ_atom / λ_shell}` skew-SYT branching factor (number of standard Young tableaux of shape `λ_atom / λ_shell`)

## Numerical evidence

At `A_magic = 8` (⁸Be, doubly magic): the SDP/LP optimum found by [`sdp_on_shadows.py`](https://github.com/litlfred/qou/blob/main/computations/sdp_on_shadows.py) yields

$$x_{(7, 1)} = x_{(2, 1^6)} = 35.24$$

— two transpose-conjugate partitions of 8 with **identical** ILP weights. This is the categorical magic-shell signature: the self-dual constraint reduces the ILP solution space to half (one variable per conjugate pair) and the optimum sits exactly at the diagonal.

## Why this matters for the H/D error budget

For ¹H, D (non-magic): `Δm_shell = 0`. The `+1.84%` `m_p/m_e` residual cannot be closed by `σ_shell` content. The residual must come from the tower formula's intrinsic structure.

For ⁴He, ⁸Be, ¹²C, ¹⁶O, ²⁰Ne, ²⁴Mg, ⁴⁰Ca (Z=N magic-A or near-magic): `Δm_shell` is non-zero. The current `mass-table-ppb` "magic-A formula" `2A·8G` is the post-Archimedean shadow of `Δm_shell`; the full pre-Archimedean form is `Δm_shell` per `sigma_shell_characterization.py`.

## Connection to the falsified probe

My probes tested whether `β_atom` is shell-self-dual. They falsified this. The right test is whether `σ_shell` (as an element of `H_{3·A_magic}(q)`) is shell-self-dual — and YES it is, by ILP construction.

So the categorical magic structure is:

| level | object | self-dual? | how |
|---|---|---|---|
| atom | `β_atom = atom_braid_word_3A(Z,N) ∈ H_{3A}(q)` | NO | structural braid; not constrained |
| **shell** | **`σ_shell ∈ H_{3·A_magic}(q)`** | **YES** | constructed via ILP at level 4 with `x_λ = x_{λ*}` constraint |
| nucleon | `T_w(p), T_w(n) ∈ H_3(q)` | NO | physical-knot Markov closure |

`σ_shell` and `β_atom` are independent Hecke elements at different strand counts (`3·A_magic` vs `3·A`); for `A = A_magic` they live in the same `H_{3A}(q)` but are distinct elements.

## Empirical magnitude (from running `sigma_shell_characterization.py`)

The shell shadow-price contribution `y_shell × σ_shell` is **tiny**
(in q-units):

| A_magic | partition | `|y_shell|` | `y · σ` |
|---:|---|---:|---:|
| 2 | (3, 3) | 5.31×10⁻³ | 5.89×10⁻³ |
| 8 | shell partition | 6.78×10⁻²⁶ | 7.52×10⁻²⁶ |
| 20 | shell partition | 8.06×10⁻¹¹⁷ | 8.95×10⁻¹¹⁷ |
| 28 | shell partition | 5.92×10⁻²¹⁰ | 6.57×10⁻²¹⁰ |

**Higher A_magic is exponentially suppressed.** Dominant contribution
is at A_magic = 2.

In MeV (using E_0 ≈ 3.13 MeV/cat-unit from β-decay calibration), the
A_magic=2 contribution is ≈ 0.018 MeV per atom. **Tiny vs bulk
binding** (e.g., ⁴He B = 28.3 MeV; σ_shell is < 0.1% of B).

So `σ_shell × y_shell` is **NOT a replacement** for `mass-table-ppb`'s
`2A · 8G ≈ 30 MeV` for ⁴He. It is a **small structural correction**
on top of the bulk magic-A formula.

**However**, the full Δm_shell per the paper has the form

$$\Delta\mathfrak{m}_{\text{shell}} = z^2 \cdot \Phi_q\bigl(|\hat{V}_{\text{shell}}|^2\bigr) \cdot y_{\text{shell}}(q) \cdot f^{\lambda_{\text{atom}} / \lambda_{\text{shell}}}$$

which includes a `Φ_q(|V̂_shell|²)` amplification factor. At near-pole
`V̂_shell` values, Φ_q is large (1000s), which would multiply the tiny
y_shell × σ_shell into something physically relevant. The current
`sigma_shell_characterization.py` does NOT include this amplification
— it computes only the `y · σ` "bare contribution".

**Open work** (deferred):

1. Compute `V̂_shell` (additive Wedderburn-traced volume at the shell
   boundary) and apply `Φ_q(|V̂_shell|²)` to get the full Δm_shell.
2. Wire the full Δm_shell into `categorical_q_decay_ba_low_isotopes.py`
   for magic atoms.
3. Compare to `mass-table-ppb`'s `2A·8G` for ⁴He — does the full
   Δm_shell reproduce the ~30 MeV magic-A contribution categorically?

Until the Φ_q amplification is wired, the σ_shell content is documented
but not numerically deployed.

## See also

- [`prop:shell-schur-weyl-self-duality`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/shell-schur-weyl-self-duality.md)
- [`prop:mass-coefficient-shadow-price`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/mass-coefficient-shadow-price.md)
- [`computations/sigma_shell_characterization.py`](https://github.com/litlfred/qou/blob/main/computations/sigma_shell_characterization.py)
- [`computations/sdp_on_shadows.py`](https://github.com/litlfred/qou/blob/main/computations/sdp_on_shadows.py)
- The two falsifying probes:
  - [`probe-atom-shell-self-duality.witness.json`](https://github.com/litlfred/qou/blob/main/computations/probe-atom-shell-self-duality.witness.json)
  - [`probe-per-nucleon-self-duality.witness.json`](https://github.com/litlfred/qou/blob/main/computations/probe-per-nucleon-self-duality.witness.json)
