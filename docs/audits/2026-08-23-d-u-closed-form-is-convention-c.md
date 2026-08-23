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

## The D-frame law is now PINNED EXACTLY at the deuteron

`markov/peel_anchor_identification_probe.py` computes `tr_M_atomic` as an
**integer-coefficient rational function of q with no anchor in it** — so its
denominator *is* the D-frame `D(u)`, not an approximation of it. For the
deuteron (numerator degree 50):

    denominator : 192*q**23*(q**2 + 1)**3      at q = u^2 ->  192 * u^46 * (1+u^4)^3

Against the C-frame law at (Z,N) = (1,1):

| factor | C-frame law | D-frame, exact | |
|---|---|---|---|
| prefactor | `2^(2A+1)` = **32** | **192** | ×6 |
| u-exponent | `18Z+21N+1` = **40** | **46** | +6 |
| cyclotomic | `(1+u²)^(3A−1)` = `^5` | `(1+u⁴)^3` | base *and* exponent |

Both fields `qou-iayk` recorded for the fresh Habiro deuteron — prefactor 192,
exponent 46 — are reproduced **exactly** by this independent exact computation.
That settles reading (a): the fresh values are not a producer defect.

It also independently corroborates the convention identification. The peel
probe writes convention C as `1/(√q + q^{-1/2})` — the *same* spelling as
`d_u_closed_form_proof.py:18` — and notes that C "would leave half-integer
powers of q behind", which is why the `(q²+1)` factorisation is itself a
structural convention test.

### The remaining open piece, stated precisely

The cyclotomic **exponent** moves 5 → 3, and clearing `z` does not explain
that. `z_D^(n−1)` with `n = 3A = 6` would give `(1+u⁴)^5`, not `^3`. The probe
says `(q²+1)` appears **"once per Markov peel"** — three peels for the
deuteron — where the C law used `z^(n−1)` — five. Those are two different
countings, and only one data point is in hand.

So the D-frame law is **exact at the deuteron and not yet general**: the
`(Z,N)` dependence of all three factors needs the other atoms. `12Z+20N+14`
fits the four recorded exponents and is now corroborated at the deuteron by
this exact route — but it remains a fit for T, ³He and ⁴He until each is
computed the same way.

## RESOLVED: the D-frame law, computed on all four atoms

Re-running `markov_peel.tr_M_atomic` per atom and factoring the denominator
(`markov/d_frame_closed_form_law_probe.py`):

| atom | Z | N | prefactor | u-exp | `(1+u⁴)^k` | C-law pref / exp / k |
|---|---|---|---|---|---|---|
| D | 1 | 1 | 192 | 46 | 3 | 32 / 40 / 5 |
| T | 1 | 2 | 768 | 66 | 4 | 128 / 61 / 8 |
| ³He | 2 | 1 | 768 | 58 | 6 | 128 / 58 / 8 |
| ⁴He | 2 | 2 | 3072 | 78 | 7 | 512 / 79 / 11 |

Fitting each factor as `aZ + bN + c` on D/T/³He and testing on ⁴He — **both
held-out predictions exact**:

```
C-frame :   2^(2A+1) · u^(18Z+21N+1) · (1+u²)^(3A−1)      [= u^(21A−3Z+1)]
D-frame : 6·2^(2A+1) · u^(20A−8Z+14) · (1+u⁴)^(A+2Z−1)
```

### The structurally interesting part

Under C the cyclotomic exponent is `3A−1`: **protons and neutrons contribute
equally**. Under D it is `A + 2Z − 1` — **a proton contributes 3, a neutron 1**.
The law becomes p/n asymmetric, where C was blind to the distinction.

This also explains the `qou-iayk` puzzle completely. ³He matched the C
exponent exactly (58 = 58) while its A=3 partner T was off by 5, which looked
like incoherence; it is simply where `20A − 8Z + 14` and `21A − 3Z + 1`
intersect, at (Z,N) = (2,1).

### What is exact and what is fitted

**Exact:** every per-atom denominator. `tr_M_atomic` returns an
integer-coefficient rational function of `q` with no anchor in it, so its
denominator *is* `D(u)`.

**Fitted:** the three `(Z,N)` closed forms. Three parameters against four
atoms is **one degree of validation each**; both passed. That is much stronger
than the original four-point exponent fit — the inputs are now exact and two
independent quantities each validate — but it is still not a derivation.

**Open:** *why* the counting gives `A + 2Z − 1` rather than `n − 1 = 3A − 1`
(the probe's own phrasing is "once per Markov peel"), and why the prefactor
picks up a uniform 6 when its C derivation — crossing-counting — is
convention-free. Both are structural questions this does not answer.

## This is the SECOND instance of a documented pattern, not a new theory

PR #5265 §0 (merged 2026-08-19) reached the same structural conclusion by a
different route, on a different object — the eigenphase rather than the D(u)
denominator:

> *"the `h²/2` anomaly is **not a defect of D**. It is the signature that D
> tracks the crossing-sign exchange, while the phase formula `α = (z−1)h/2` —
> written in the C frame, where `z` does not move under bar — was carried over
> unchanged. **It is the phase formula that needed re-deriving, not the
> convention.**"*

That agent also recorded having had it backwards first: *"The opposite of how I
framed it one commit earlier, where D 'failed' the test and C 'passed' it. Both
facts were right; the value judgement attached to them was backwards."*

`qou-iayk` is the same inversion one object over. A C-frame formula carried
into D produces an apparent "D is broken" signal; the formula is what broke.

**The generalisable rule:** when D-frame output contradicts a landed result,
check whether the *result* was derived from `z` before concluding the output
is wrong. Two for two so far, on independent objects.

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

- The `(Z,N)` closed forms are fits over exact per-atom data (one degree of
  validation each), not derivations. The counting rule behind `A + 2Z − 1`
  and the uniform 6 in the prefactor are both open.
- The Habiro regeneration is **not** unblocked by this alone — it should land
  together with the re-derived law, or the same mismatch recurs.
