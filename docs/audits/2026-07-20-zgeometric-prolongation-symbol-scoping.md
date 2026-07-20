# z-geometric scoping: is the C1 carrier the Seiberg–Witten prolongation symbol?

**Date:** 2026-07-20
**Branch:** `claude/qlift-borel-kernel-derivation-2026-07-20` (PR #4139)
**Bean:** `qou-h5cf` (z-geometric)
**Status:** SCOPING — decomposes the keystone's deepest residual into the
smallest attackable sub-claim vs. the genuine geometric-analysis walls. Makes
NO identification claim (anti-laundering). Companion probe:
[`computations/probes/zgeometric_ramification_parity_probe.py`](../../computations/probes/zgeometric_ramification_parity_probe.py).

## 1. What the geometric identification requires

`conj:qdifference-kernel-prolongation-symbol` asks that the binding q-difference
kernel `R` (proved carrier **C1**: `[m+2]_q b_{m+2} = b_{m+1} + b_m`, Lean
`qlift_normalized_kernel_exists`) BE the **symbol of the jet-prolongation
operator** `J^n E → J^{n+1} E` of the SW connection — equivalently the local
monodromy/Stokes datum of the prolonged SW differential `λ_SW^(n)` at the
branch-point poles on `S_c ≅ P¹`. Unpacked, a genuine derivation must supply:

- **(G1) A prolongation operator.** An operator `D : J^n E → J^{n+1} E` lifting
  the SW connection to the jet tower over the color spectral curve `Σ`
  (`P = X³+(z+1)X²+(z²+z+1)X+(z³+z²+z+1)`). The **classical** lift `D = d/dz`
  exists but is **proved wrong** (§2). So (G1) demands a **non-classical**
  (q-difference) prolongation — which the corpus does not construct.
- **(G2) Its symbol at a ramification point.** At `z = z_c + t²` (simple branch,
  local coord `t`) the principal symbol of `D` is read off the leading Laurent
  behaviour in `t`. The jets acquire poles (`X^(1) = (dX/dt)/(2t)`, order rising
  by 2 per jet), so the "symbol" is the leading-coefficient / connection-matrix
  datum on the `t`-punctured disk.
- **(G3) Symbol coefficients = C1 coefficients**, `prolongationSymbol j = kernel j`
  (the Lean class field `kernel_eq_symbol`), derived — not fitted to reproduce
  the binding terms. Anti-laundering: C1 is *already* fixed by the binding
  recurrence, so a match is only meaningful if the symbol is computed from `Σ`
  **independently**.

## 2. What the corpus already has toward it

| Piece | Statement | Status |
|---|---|---|
| `prop:sw-classical-jet-exactness` | classical jets `λ_SW^(n)=d(X^{(n-1)})` are **exact** ⇒ all residues/periods **=0** ⇒ ≠ binding period `I(m)/m>0` | **proved** (Lean `classical_jet_period_zero`, `classical_jet_period_ne_lw`; `fresidue_fderiv` over generic `CommRing`) |
| `prop:sw-period-residue-sum` | `a_D^(n)=∮λ_SW^(n)=2πi Σ Res`; jet degree `n` = body order | proved-conditional (residue-sum shape a hypothesis) |
| `prop:mi-sw-abelianisation` / `jet-sw-tau-decomposition` | MI-integral abelianises to `Σ_n a_D^(n)`; `τ` observes the jet tower | proved-conditional |
| C1 exists / normalization | `[m+2]_q b_{m+2}=b_{m+1}+b_m`; `N(n)=(n−1)!` | **proved** (`qlift_normalized_kernel_exists`, `binding_carrier_satisfies_kernel`) |
| gauge-gap synthesis (5 routes) | C1 ≢ GGM as q-difference modules (isoclinicity `{½,½}` vs `{−1,+1}`); favors **R1** = C1 is its own Gevrey-½ carrier | scope-(b), invariant named |
| Door-iv/v | `C1⊗C1` = GGM up to a single diagonal **`(−1)^m` bar-parity** twist (cosh/sinh) | machine-measured, exact |

The classical-jet exactness result is the load-bearing **negative constraint**:
it proves (G1)'s classical candidate dead, forcing the non-classical prolongation
— i.e. the corpus has closed the "which prolongation" question down to
"q-difference," but has **not** built that q-difference prolongation from `Σ`.

## 3. Decomposition — smallest sub-claims vs. research walls

**Formalizable / attackable now (build on existing infra):**

- **S1 — ramification monodromy = `(−1)^n` character (the Door-v residual is
  geometric).** At `z=z_c+t²` the covering monodromy is `t → −t` (one z-loop =
  half a t-loop), acting on `a_k t^k` by `(−1)^k`. And classical `d/dz=(1/2t)d/dt`
  shifts the `t`-exponent by **exactly −2**, hence **preserves `t`-parity** — so
  the classical jet can never generate `(−1)^n`. **Verified exactly** in the
  probe (index-shift-by-2 on `t^0..t^8`, jets `n=1..4`; genuine simple branch of
  the color cubic, `|P_X(X0,z_c)|≈6e−21`). This identifies Door-v's *single named
  residual* (`C1⊗C1` vs GGM differ by `(−1)^m`) with the **ramification covering
  monodromy** — a finite, algebraic bridge, formalizable by extending the proved
  `fresidue`/`jet` model with a parity involution. This is the concrete
  attackable sub-claim.
- **S2 — a non-classical jet whose symbol satisfies a depth-2 q-recurrence.**
  Given ANY candidate q-difference prolongation `D_q`, checking that its symbol
  obeys `[m+2]_q(·)=(·)+(·)` is a finite coefficient comparison (Lean/`sympy`),
  once `D_q` is written down. Attackable *conditional on* (G1).

**Genuine research walls (no Mathlib/corpus tooling):**

- **W1 — construct the q-difference prolongation `D_q` from `Σ` (the crux of
  G1).** There is no corpus object "q-jet bundle / q-de Rham prolongation of the
  SW connection." Classical jet bundles `J^n E` and their prolongations are
  standard; their **q-deformation** (Aomoto q-connections, scheme-theoretic
  q-jets, q-D-modules) is not in Mathlib and only sketched in the literature.
  Deriving `D_q` *from the geometry* — not reverse-engineering it from C1 — is
  the multi-month piece.
- **W2 — principal-symbol / D-module calculus at a ramified pole (G2).** Reading
  a symbol from local monodromy of an irregular q-connection needs the
  Ramis–Sauloy–Zhang local classification machinery operationally (already cited
  in the synthesis for the *obstruction*, but never as a *constructive* symbol
  extractor). None of this is formalized.
- **W3 — the independence/anti-fit obligation (G3).** Even with `D_q` and its
  symbol, showing `symbol = C1` is only a derivation if the symbol is computed
  without target-matching. The five-route synthesis already shows C1 is a
  *distinct* module from the GGM face, so the identification is with the
  **prolongation-symbol face specifically** — which must be pinned by `Σ`, not by
  the binding terms. This is a correctness wall, not just labor.

## 4. Honest verdict

- **The full identification is a multi-month geometric-analysis program.** Its
  crux (W1: constructing the q-difference prolongation of the SW connection on
  `Σ`, and W2: extracting its symbol) requires q-jet-bundle / q-D-module symbol
  calculus that is absent from both Mathlib and the corpus. It cannot be closed
  by a probe or a short Lean lemma.
- **One sub-claim IS attackable now — S1.** The Door-v `(−1)^m` bar-parity
  residual — the *sole measured difference* between the C1 tensor-square and the
  GGM carrier — is exactly the **ramification covering monodromy `t→−t`**, while
  classical `d/dz` provably preserves `t`-parity. This is finite, algebraic, and
  formalizable on the already-proved `fresidue`/`jet` residue model (add a
  `t→−t` involution; show the classical jet commutes with it and the `(−1)^n`
  eigen-grading is the covering character). It does **not** close the keystone,
  but it upgrades the framework's cosh/sinh (bar-even mass / bar-odd decay)
  distinction from a *measured* algebraic residual to a *geometric* statement
  about the branch-point cover — the first genuine bridge from C1 to the SW
  ramification geometry, and the natural next PR.
- **Anti-laundering restatement.** Nothing here claims C1 = prolongation symbol.
  The classical prolongation is proved *excluded*; the non-classical one is *not
  constructed*; S1 identifies *one shared invariant* (parity monodromy), not the
  operators. The keystone stays a conjecture.

## 5. Discipline

- **Corpus-grep:** `prolong` swept across `content/`, `computations/`,
  `docs/audits/`; the geometric-identification trail is the brings-surface SW
  blocks + this branch's 2026-07-20 qlift files. No prior attempt on the
  ramification-parity bridge (S1); no closed item re-opened.
- **Anti-fit:** the probe is parameter-free (exact `sympy`/`mpmath` structural
  check, no AME data, no wiring, EXPLORATORY). S1's claim is scope-(b) with its
  invariant (covering character `(−1)^k`) named; W1–W3 are labeled research
  walls, not refutations.
