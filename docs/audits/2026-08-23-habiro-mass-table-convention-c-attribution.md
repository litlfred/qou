# The committed mass-table Habiro witnesses are convention C — attribution settled

**Date:** 2026-08-23
**Bean:** `qou-iph3`
**Settles:** the attribution left open by [PR #5526](https://github.com/litlfred/qou/pull/5526)
**Probe:** [`computations/habiro/habiro_mass_table_convention_attribution_probe.py`](../../computations/habiro/habiro_mass_table_convention_attribution_probe.py)

## Verdict

Every committed `computations/habiro-coefficients-*.witness.json` on `main`
(@ `b4f9e350e9`) was built under **convention C** (`z = √q/(q+1)`).

```
committed reproduced by convention C : 25/25
committed reproduced by convention D : 2/25
atoms carrying at least one interface : 23   ... all convention C : True
D-matches are interface-free only     : True
```

The two atoms that also reproduce under D are the proton and the neutron. Their
`canonical_interface_kinds` is `[]`, so the interface product is the empty
product `1` and the two conventions make the *same* statement about them. **Every
atom that has an interface at all is convention C.**

This is the "test the answer, not the source" method AGENTS.md prescribes for
this class. It needs no `z` grep, no source archaeology, and no resolvable
`commitSha` — the convention is read off the committed numbers themselves.

## What #5526 got wrong, and why the error was reasonable

#5526 declined to attribute the move, on this argument:

> the deuteron's only interface factor **is** `z`, and the deuteron is
> **unchanged**. A C→D change in `z` would have moved it. The difference
> therefore sits in the `negative`/`averaged` branch — `(z − h)` / `(z − h/2)`
> — not in `z`.

The premise is false: **the deuteron did move.** It is unchanged only in
`p_in_u` / `habiro_coefficients`, which is the one field that *cannot* move for
an all-`positive` atom. From the #5526 diff of the deuteron witness itself:

| field | committed (C) | regenerated (D) |
|---|---|---|
| `tr_M_at_q0` | `0.565089262867502` | `0.6933894087146489` (**+22.7 %**) |
| `denom_in_u` | `16u⁴⁵ + 16u⁴³ + 32u⁴¹ + 32u³⁹ + 16u³⁷ + 16u³⁵` | `16u⁴² + 48u³⁸ + 48u³⁴ + 16u³⁰` |
| `tr_M_in_q` denominator | `16q^(35/2)·(q+1)·(q⁴+2q²+1)` | `16q¹⁵·(q²+1)·(q⁴+2q²+1)` |
| `p_in_u` | *unchanged* | *unchanged* |

The half-integer exponent `q^(35/2)` and the `(q+1)` factor are the convention-C
signature; `q¹⁵` and `(q²+1)` are D's. Old `denom_in_u` factors as
`16u³⁵(u²+1)(…)`; new as `16u³⁰(u⁴+1)³` — and `q+1 = u²+1` against
`q²+1 = u⁴+1` is precisely the C-vs-D distinction carried into `u`.

### The 16/4 split is the signature of the swap, not evidence against it

Habiro extraction sets `p(u) := u^shift · denom · tr_M(u²)`.

- **All-`positive` atom.** Interface product is a pure power `z^k`. Swapping
  `z_C → z_D` rescales `tr_M` by a rational function, which `denom` absorbs
  wholesale. The numerator `p(u)` — hence every `a_m` — is untouched.
- **Any `negative`/`averaged` interface.** `z` now sits inside a *sum*
  `(z − h)`. The numerator itself changes, so `p(u)` and the coefficients move.

So "16 move, 4 do not" is exactly what a C→D swap predicts. The four that hold
still are the two interface-free atoms (proton, neutron) plus the two
all-positive ones (deuteron `['positive']`, ³He `['positive','positive']`).
Comparing coefficients alone is blind to the swap on precisely that subset.

The general lesson is the one this repo keeps re-learning: **a field that is
invariant under the change you are testing for cannot be the field you test
with.** `reconstruction_matches: True` on both generations is likewise not
discriminating — it says each `p(u)` is a self-consistent expansion of its own
input, which is true under either convention.

## Consequence #5526 does not cover: merging it leaves a mixed table

The producer's `ATOMS` list has **20** entries. `main` carries **25** committed
atom witnesses. Merging #5526 as-is regenerates 20 into convention D and leaves
five in convention C:

| atom | Z | N | interfaces |
|---|---|---|---|
| `helium-6` | 2 | 4 | `p p n n n` |
| `boron-12` | 5 | 7 | `p⁵ n⁶` |
| `carbon-14` | 6 | 8 | `p⁶ n⁷` |
| `nitrogen-12` | 7 | 5 | `p⁷ n⁴` |
| `oxygen-14` | 8 | 6 | `p⁸ n⁵` |

All five carry `negative` interfaces, so all five are genuinely C-valued — not
C≡D coincidences. A silently mixed mass table is a worse state than a uniformly
stale one: it is the straddle AGENTS.md forbids inside a single quantity, one
level up, and nothing in the tree flags it.

**Either regenerate all 25 (add the five to `ATOMS`) or regenerate none.**

## Scope of this finding

Scope-(a) in the AGENTS.md sense, stated precisely:

- **Established.** Every committed atom witness on `main` is convention C. The
  #5526 regeneration is a C→D correction, and it is a correction — D is
  canonical per the owner ruling of 2026-08-15 (R1).
- **Established.** The 16/4 split is fully explained by C→D plus the
  numerator/denominator argument above. No second cause is needed, and none is
  in evidence.
- **NOT established.** *When* the producer moved from C to D, or in which
  commit. `_markov_z_q` carries D today and documents its own migration, but
  this probe reads outputs, not history, and `scriptCommitSha` on these
  witnesses is subject to the rebase-rewrite class. Unnecessary for the merge
  decision: what the committed numbers *are* is settled regardless of when they
  became that.
- **NOT established.** Whether any downstream consumer's conclusions change.
  Consumers are overwhelmingly audit docs; `tr_M_at_q0` moving 22.7 % on the
  deuteron is large enough that this needs its own pass.

## Correction to a claim I made in session

I was briefed that *"'the mass-table witnesses were convention-C' is not
something the evidence supports"*, on the deuteron argument above. That briefing
was inherited from #5526 and is wrong; the evidence supports it at 25/25. The
guard it was protecting against — writing the attribution on the strength of
#5526's *own* data — was well placed: #5526's data really does not settle it.
It took a different measurement, on the field the swap actually moves.

## Reproduce

```bash
python3 -u computations/habiro/habiro_mass_table_convention_attribution_probe.py
```

Exact arithmetic throughout — no float. The identity is tested at three
perfect-square rationals (`q = 49/25`, `121/9`, `9/4`) so that `√q` is exact and
convention C is representable without a radical.
