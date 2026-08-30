---
# qou-h9p8
title: 'GAP: rem:markov-axioms-primitive + thm:jones-markov-trace stipulate convention C while the mass fibre forces D — the definitional-side half of the qou-3qrv owner decision'
status: completed
type: task
created_at: 2026-08-08T13:13:32Z
updated_at: 2026-08-19T00:00:00Z
---

## What is open

The corpus has **two** definitional pins for the Markov-trace stabilisation
parameter, both stipulating convention **C**
($z = 1/(q^{1/2}+q^{-1/2}) = q^{1/2}/(q+1)$, the full-Hecke Ocneanu / Wenzl
$z$-trace):

| block | file:line |
|---|---|
| `rem:markov-axioms-primitive` | `content/quantum-observable-universe/braids-and-knots/markov-axioms-primitive.md:5` (axiom 3) |
| `thm:jones-markov-trace` | `content/quantum-observable-universe/braids-and-knots/jones-markov-trace.md:7` |

The mass channel's production code computes convention **D**
($z = q^3/(q^2+1)$, $y_{(1^3)} = 0$), and
`docs/audits/2026-08-08-mass-fibre-dimension-forces-convention-d.md` shows D is
forced once the mass fibre is the 2-dimensional $\mathrm{SU}_q(2)$ fundamental.
So the `mass` channel is `disputed` in
`docs/coordination/trace-convention-registry.json`: definitional C, production D.

**Open question: does the definitional side move to D, and if so where?**

## What was attempted (2026-08-08, branch `claude/fix-markov-z-stipulation-2026-08-08`)

The naming half was fixed; the value half was **declined as not an agent's call**.
Full reasoning: `docs/audits/2026-08-08-markov-axioms-naming-vs-z-value.md`.

- Both blocks now say plainly *which* member of the Ocneanu family their $z$ is,
  and `jones-markov-trace.md`'s outright false sentence ("computes the Jones
  polynomial of the closure up to framing", at $z = z_C$ where
  $y_{(1^3)} \neq 0$) was corrected.
- Both pins are now `doc_claims` rows under registry rule R6, so they cannot
  drift apart.
- No $z$ was changed; no production value moved
  (`canonical_mass.proton_mass_mev() = 938.2720894273243`, unchanged).

## Why it was not closed

1. `docs/audits/2026-08-08-trace-convention-registry-and-doc-fix.md` §6 follow-up
   1 reserves it: *"either establish the TL premise, in which case D is forced and
   the definition chain should be corrected to say so, or accept C and take the
   −197 ppm. **Do not decide by match.**"* Bean `qou-3qrv`.
2. The pro-D audit explicitly scopes D to the *fibre*, not to $\mathrm{H}_n(R,q)$:
   *"It is **not** a claim that C is not a Markov trace on $\mathrm{H}_3(q)$ — it
   is one … and every statement about it as such stands."* Both pinning blocks are
   stated on the full $\mathrm{H}_n(R,q)$.
3. Blast radius of the definitional route, measured: **≥ 8 corpus sites** stipulate
   or derive from the C value — `thm:jones-markov-trace` (cited *by* the other
   pin) and its `.lean`, `prf:trm-hopf-sigma1-sq-closed-form`,
   `prf:trace-locality-meets-gs-nonlocality`,
   `prf:hecke-satisfies-blitvic-hypothesis`,
   `prop:centered-hecke-variance-positive` (+ proof + table data),
   `prf:algebraic-gns-embedding`, and
   `rem:bar-involution-c5-algebraic-identities` — whose "the Markov parameter $z$
   is bar-invariant" is **true for C and false for D** ($\bar z_D = 1/(q^3+q)$).
   It would also flip the `binding` channel from `agreed` to `disputed`, since
   binding's `definitional_source` is that same line while binding production is C.

## Next honest step

Not a fix — a decision, then a chapter-wide pass:

1. Owner rules on `qou-3qrv` (C production, or D definition, or an explicit split).
2. **If D:** work the ≥ 8-site list above in one commit, `thm:jones-markov-trace`
   and its Lean sibling first, and re-source `binding`'s registry row in the same
   commit so it does not silently flip to disputed.
3. **Alternative worth considering instead of either:** make the
   braids-and-knots chapter carry $z$ **free** in the generic block, with two
   named specialisations (C for the full-Hecke / binding channel, D for the
   $\mathrm{SU}_q(2)$-fibre / mass channel). Then neither channel's definition is
   wrong and the registry's `definitional_convention` becomes a per-channel
   selection rather than a corpus-wide stipulation. This is the only option that
   makes the mass/binding split *expressible* rather than merely documented.

## Verified facts to reuse (do not re-derive)

$h = q - q^{-1}$, $q_0 = 1.1099785827513808$ (proton pin), sympy-exact:

| | $z$ | $z(q_0)$ | $z_{-} = z - h$ | $z_{-}(q_0)$ | bar-invariant |
|---|---|---|---|---|---|
| C | $q^{1/2}/(q+1)$ | $0.49932033418369445250$ | $\frac{q^{3/2}-q^3-q^2+q+1}{q(q+1)}$ | $0.29026003538805515083$ | yes |
| D | $q^3/(q^2+1)$ | $0.61268803714646524365$ | $1/(q^3+q)$ | $0.40362773835082594197$ | no |

- $z_{-}^{D} = 1/(q^3+q) = \bar z_D$ **exactly** — under D the two stabilisation
  parameters are bar-conjugate. No analogue for C.
- Convention-**in**dependent, so untouched by any decision: the root pair of
  $z\,z_{-} = 1$ ($z = q$, $z = -q^{-1}$; depends only on $h$), the derivation
  $z_{-} = z - h$ from $\sigma_n^{-1} = \sigma_n - h$, and the $z^k$
  strand-appending factor.

## CLOSED — by the owner ruling, not by this bean's work (recorded 2026-08-19)

Filed 2026-08-08 against a real gap: `rem:markov-axioms-primitive` and
`thm:jones-markov-trace` both stipulated convention **C** while the mass fibre
forces **D**.

**The owner ruling of 2026-08-09 excised convention C repo-wide**, and the
2026-08-15 ruling made D canonical. Verified on `main` at the time of this
note: both blocks now lead with `z = q^3/(q^2+1)` and carry the excision
explicitly; the C form survives in each only as documented history, not as a
live stipulation. There is nothing left to do here.

Salvaged alongside its audit doc from PR #4767, which was closed as superseded.
Landing this bean at `todo` would have put a closed item back into the queue —
the failure mode the corpus-grep checklist exists to prevent — so it is
recorded `completed` instead.
