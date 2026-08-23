# The D(u) closed-form law is convention-C by construction

**Bean:** `qou-cxon`. **Adjudicates:** `qou-iayk` (blocked 2026-08-21).
**Answer to "do we need to re-derive the closed-form law in D?": YES — for one
of its three factors it is not a judgement call, it is a definition.**

## The block being adjudicated

`qou-iayk` attempted the Habiro convention-D regeneration, then **stopped and
reverted**, on the grounds that the fresh values break a landed law that the
old witness satisfies exactly:

```
D(u) = 2^(2A+1) · u^(18Z+21N+1) · (1+u²)^(3A−1)
```

with the deciding observation recorded as: *"the EXPONENTS are off by +6, +5,
0, −1. An irregular offset is NOT explainable by a normalisation, and one atom
(³He) matches exactly while its A=3 partner (T) is off by 5."*

That agent left two readings and said they could not adjudicate:

- **(a)** the producer has a defect beyond the parser;
- **(b)** a deeper convention change invalidates the law, which needs
  re-deriving in the new frame.

**(b) is correct. (a) is disfavoured by an independent computation.**

## 1. The law's three factors have different provenance — only one is at issue

Read from `computations/d_u_closed_form_proof.py` itself:

| factor | where it comes from | convention-dependent? |
|---|---|---|
| `2^(2A+1)` | counting averaged crossings, each `(σ+σ⁻¹)/2` giving ½ | **no** — braid word only |
| `(1+u²)^(3A−1)` | *"the Markov/Ocneanu trace formula z^(n−1) at q = u²: with z = u/(1+u²) and n = 3A, clearing the denominator"* (lines 339-340) | **yes — it IS the cleared denominator of z** |
| `u^shift` | *"left as an open structural question (depends on the Hecke-NF reduction; varies by 3 between T and ³He at A=3)"* | **never derived, in either frame** |

## 2. That `z` is convention C — verified, not assumed

`d_u_closed_form_proof.py:18` writes `z = 1/(q^(1/2) + q^(-1/2))`. That is the
**detector-blind C spelling** catalogued in #5124:

```
1/(√q + 1/√q)  ≡  √q/(q+1)  =  z_C        (0.499320 at q₀)
                   z_D = q³/(q²+1)          (0.612688 at q₀)
```

At `q = u²`:

```
z_C = u/(1+u²)    -> clearing gives (1+u²)^(3A−1)      <- the landed law
z_D = u⁶/(1+u⁴)   -> clearing gives (1+u⁴)^(3A−1)      <- the D-frame law
```

So the landed law **encodes convention C in its structure**. Testing D-frame
output against it is testing it against the wrong frame; the fresh values do
not "break" the law, they satisfy a different one.

## 3. The "irregular offset" is not irregular

Fit `δ = aZ + bN + c` on three atoms, then predict the fourth:

```
fit on D, T, ³He :  δ = 13 − 6Z − N
held-out ⁴He     :  predicted −1, actual −1   EXACT
```

so the fresh exponent is `12Z + 20N + 14`, exact on all four, small integers —
the same shape as the C-frame `18Z + 21N + 1`. The "³He matches exactly while
its A=3 partner T is off by 5" puzzle is simply where `13 − 6Z − N` crosses
zero at (Z,N) = (2,1).

**Weight this correctly:** three parameters against four points is one degree
of validation. It is evidence the fresh data is *structured* rather than
garbage — which is what bears on reading (a) — and it is **not** a derivation
of the D-frame law. Do not wire `12Z + 20N + 14` anywhere as canonical.

## 4. Independent confirmation that the fresh values are D-correct

`computations/markov/peel_anchor_identification_probe.py` — different code,
different author, its own landed assertion `peel_denominator_is_convention_D`
— computes the deuteron peel denominator. Re-run on this tree:

```
denominator : 192*q**23*(q**2 + 1)**3
```

**192 is exactly the fresh Habiro deuteron prefactor.** The C-frame value is
`2^(2A+1) = 32`, and `192/32 = 6` — the uniform "6×" `qou-iayk` recorded as
unexplained. It is not unexplained: it is the D-frame value, reached by code
that never touched the Habiro producer.

Note this also means the `2^(2A+1)` prefactor — the factor whose derivation is
convention-*free* — moves as well. Crossing-counting alone therefore does not
determine it, which is a genuine open sub-question this audit does **not**
close.

## What follows

1. **Re-derive the law in D.** The `(1+u²)^(3A−1)` factor becomes
   `(1+u⁴)^(3A−1)` by the same argument the C proof uses. That much is
   mechanical.
2. **The prefactor needs a real derivation**, not a re-count: the peel probe
   says 192 where crossing-counting says 32.
3. **The u-shift stays open**, as it was in C. Any claim about it — including
   §3 above — is a fit until derived.
4. **`qou-iayk`'s revert was still the right call at the time.** It declined to
   land values it could not justify. What this audit supplies is the
   justification it was missing, from a source that agent did not consult.

## Not claimed

- No re-derived D-frame law is landed here; this establishes that one is
  *needed* and identifies which factor is definitional.
- The Habiro regeneration is **not** unblocked by this alone — it should land
  together with the re-derived law, or the same mismatch recurs.
