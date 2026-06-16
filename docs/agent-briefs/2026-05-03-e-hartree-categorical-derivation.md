# Agent brief: categorical derivation of E_h ∝ m_e c² α² via J¹ vanishing

**Fork point:** branch `claude/improve-charge-precision-aLyqu` of
litlfred/qou at commit `bc8c260abc4b30a5d529bbd1ba3c0a8ed5a0d2bd`.
PR #529 ([github.com/litlfred/qou/pull/529](https://github.com/litlfred/qou/pull/529)).

## Background — read these blocks first

The PR audited the QOU framework's α_EM formula and demoted previous
closed-form attempts (Form A: Chern-Simons κ; Form B: gluon-octet
$45 \cdot [3]_q \cdot \ldots$) to conjectures because their derivations
were unjustified or post-hoc. The bare formula
$1/\alpha = q \cdot [9]_q \cdot [10]_q$ (singlet idempotent / Bring
force-carrier complexity) is rigorously derived but has a 0.155%
residual against CODATA.

A current numerical lead suggested $1/\alpha \approx q \cdot [9]_q \cdot [10]_q + 2/(3\pi)$
(4.2 ppm) but this introduces $\pi$ and **violates the algebraic ring**
$R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$ in which the QOU
framework lives. So the "$+2/(3\pi)$" form is structurally wrong
even if numerically close.

A pure-algebraic candidate emerged: $1/\alpha \approx q \cdot [9]_q \cdot [10]_q + q/[5]_q$
(1.2 ppm). Still not exact, but inside R.

## Core directive: NO empirical / fitting / numerology

Every coefficient must be derived from QOU categorical structure.
No $\pi$, no transcendentals, no PSLQ-fitting that produces post-hoc
identifications. If you can't derive it from category, mark it open.

## Your task: categorical derivation of E_h ∝ m_e c² α² for molecular binding

### What's currently asserted (without categorical derivation)

In `computations/substrate/hecke_core.py:198`:

```python
E_HARTREE_EV = 511000.0 * alpha_em**2   # Hartree energy (eV)
```

This is the standard physics scale ($m_e c^2 \alpha^2$) — derivable
from the Bohr-radius / virial-theorem argument in non-relativistic QED.
But it is currently **used as input** in the QOU molecular-binding code
(`co2-molecular-binding.py`, `h2-binding-energy` via `h2-lp-dual-binding`,
etc.), not derived from QOU categorical principles.

### What we need

A categorical derivation of *why* molecular binding scales as $\alpha^2$
and **NOT** $\alpha^1$ — specifically, an argument from the QOU
structure that the leading $\alpha^1$ contribution **vanishes**, leaving
$\alpha^2$ as the natural scale.

### Hypothesis (user's intuition, to test)

The 1st-order jet / slice contribution to the molecular binding LP/SDP
dual at the brane vanishes by some categorical-symmetry argument
(perhaps an antiparticle-crossing reversal symmetry, or a chirality
involution, or a Frobenius-pairing antisymmetry). The first non-zero
contribution is at 2nd order, giving $\alpha^2$ scaling.

Concretely: in the LP/SDP for binding (e.g. h2-lp-dual-binding, see
`computations/h2_lp_dual.py` if exists), expand the
dual variable $y_{\text{cov}}$ in powers of $\alpha_{EM}$ around the
bare/decoupled limit. Show:

- **Order $\alpha^0$:** bare separated atoms (no binding)
- **Order $\alpha^1$:** vanishes by [some categorical reason] ← this is the open step
- **Order $\alpha^2$:** leading binding contribution = $E_h$ scale

### Concrete files to read

```
content/quantum-observable-universe/molecular-construction/h2-lp-dual-binding.md
content/quantum-observable-universe/molecular-construction/ilp-covalent-bond.md
content/quantum-observable-universe/molecular-construction/co2-lp-dual-binding.md
content/quantum-observable-universe/molecular-construction/molecular-braid.md
content/quantum-observable-universe/braids-and-knots/operator-selection-lp.md
content/quantum-observable-universe/braids-and-knots/lp-dual-stability.md
content/quantum-observable-universe/braids-and-knots/antiparticle-crossing-reversal.md
content/quantum-observable-universe/braids-and-knots/spectral-sequence-collapse.md
content/quantum-observable-universe/braids-and-knots/curvature-rank-gb-stratification.md
content/quantum-observable-universe/braids-and-knots/commutative-chirality-vanishes.md
content/quantum-observable-universe/braids-and-knots/schur-weyl-vanishing.md
computations/substrate/hecke_core.py        # E_HARTREE definition
computations/h2_lp_dual.py        # if exists
computations/co2-molecular-binding.py
```

The vanishing arguments (`commutative-chirality-vanishes.md`,
`schur-weyl-vanishing.md`) are likely highly relevant — they give
existing categorical-vanishing results that may extend to the
EM-coupling expansion.

### Deliverable

Write up your derivation attempt as content blocks under
`content/quantum-observable-universe/descartes-universe/`:

1. `e-hartree-categorical-derivation.md` (and `.ts`) — either:
   - a `proposition` with a complete categorical proof that
     $E_h \propto \alpha^2$ with the $\alpha^1$ vanishing argument, OR
   - a `conjecture` documenting the partial derivation and what's
     needed to close

2. (optional) `j1-vanishing-em-coupling.md` (and `.ts`) — the specific
   $J^1$ vanishing lemma if you can prove it

3. (optional) Solve the $H_2$ binding SDP explicitly and show the
   $\alpha$-expansion structure

Both blocks must:

- Reference upstream propositions correctly (use the existing
  `def:` / `prop:` / `rem:` labels)
- Stay inside $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$ — NO $\pi$,
  no transcendentals
- Be honest: if a step isn't derivable, mark it as open; do not paper
  over with numerology
- Validate: `cd content && bun run validate quantum-observable-universe`
  must pass
- Register in `descartes-universe.ts` chapter manifest

### Coordination

The main thread (parent agent) is on `claude/improve-charge-precision-aLyqu`.
They may push concurrent commits. Periodically rebase:

```bash
git fetch origin claude/improve-charge-precision-aLyqu
git rebase origin/claude/improve-charge-precision-aLyqu
```

When done, push to a NEW branch (don't push to
`claude/improve-charge-precision-aLyqu`):

```bash
git checkout -b claude/em-coupling-alpha-squared-derivation
git push -u origin claude/em-coupling-alpha-squared-derivation
```

Then create a PR for review against `claude/improve-charge-precision-aLyqu`
(NOT main):

```
gh pr create --base claude/improve-charge-precision-aLyqu \
             --head claude/em-coupling-alpha-squared-derivation \
  --title "Categorical derivation: E_h ∝ α² via J¹ vanishing in molecular SDP" \
  --body "..."
```

Or use `mcp__github__create_pull_request` with
`base=claude/improve-charge-precision-aLyqu`.

### Time budget

This is research; you may not close it. Aim for either:

(a) a complete categorical proof of the $J^1$-vanishing if the algebra
    works out, OR
(b) an honest partial derivation that pinpoints the exact missing step
    (e.g., "the antisymmetric channel under crossing-reversal has zero
    $\alpha^1$ pairing IF [specific lemma X holds], reducing to a
    Frobenius-trace identity that needs to be checked").

Either outcome is valuable.

If the $J^1$-vanishing argument turns out to be wrong, REPORT IT —
that's also useful data. Do not fudge.

Good hunting.
