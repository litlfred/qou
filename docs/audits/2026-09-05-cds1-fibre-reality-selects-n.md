# What selects N on the fibre locus — reality does, and it excludes the required phase

**Bean:** `qou-cds1` / `qou-pdix` route 5.
**Probe:** [`computations/qbeta/qbeta_fibre_reality_selects_n_probe.py`](../../computations/qbeta/qbeta_fibre_reality_selects_n_probe.py) (4/4).
**Scope: (a)**, conditional — see the last section.

## The question, and the method that keeps it honest

[#6755](2026-09-05-cds1-fibre-route5-unit-circle.md) established that route 5's
fibre locus is `|q| = 1` exactly, and left one arithmetic question: on the
root-of-unity sublocus `q = e^{2πik/N}`, what selects `N`? It recorded `1/111` as
the only low-denominator candidate and **refused to search for a reason it should
be 111**, on the arc's own rule that a target may be checked *against* but never
searched *on*.

This does not search on the target either. It asks what the **framework**
constrains on `|q| = 1`, derives `N` from that alone, and compares only
afterwards. **`θ` does not appear anywhere in the derivation.**

## The constraint the framework imposes on itself

`Q_β` is a measured Q-value, so it is real. Wherever the ladder is evaluated, its
Form-A baseline must therefore be real:

```
Q_A / m_e  =  |q² − 2q − 1| · (q + 1) / (2q³)
```

On `|q| = 1` that is one real equation in `φ = arg q`, with an exact solution set
— and the answer depends on how the modulus is read.

**Reading A — the form as written, modulus kept.** `|q²−2q−1|` is real by
construction, so `Q_A` is real iff `(q+1)/q³` is:

```
Im[(q+1)/q³]  =  −(sin 2φ + sin 3φ)  =  −2 sin(5φ/2) cos(φ/2)
```

(the factorisation verified symbolically, not asserted). Zero exactly at
`φ = 2πm/5` and `φ = π` — **the fifth roots of unity. N = 5**, with the
degenerate `N = 2`.

**Reading B — analytic continuation, modulus dropped.** The modulus makes `Q_A`
**non-holomorphic** in `q`, which is already reason to doubt carrying the form as
written onto a fibre where `q` is a formal variable. Continuing analytically:

```
Im[(q²−2q−1)(q+1)/(2q³)]  =  (2 cos φ + 3) · sin φ · cos φ
```

and `2 cos φ + 3` has minimum `1 > 0`, so the zeros are `sin φ cos φ = 0`:
`φ ∈ {0, π/2, π, 3π/2}` — **the fourth roots. N = 4**, with `N = 1, 2`.

**So `N` *is* selected — by a reality condition, with no fit anywhere — but the
two readings disagree.** That disagreement is a real open question about the
framework: is the `|·|` part of the object, or an archimedean artifact? Reported,
not resolved.

## Only then, the comparison

| reading | nearest admissible nonzero phase | vs required `θ = 0.0566173` |
|---|---|---|
| A (`N = 5`) | `2π/5 = 1.256637` | **22.20× too large** |
| B (`N = 4`) | `π/2 = 1.570796` | **27.74× too large** |

**The required phase is in neither admissible set, and `N = 111` is excluded
under both.** That retires the "neither excluded nor evidence" status #6755 gave
it — conditionally, per the scope below.

## Scope, and what this is not

**(a)**, and the condition is load-bearing: the exclusion holds for anyone who
requires `Q_A` real **on** the fibre locus. A mechanism that computes on the
fibre and projects to a real observable **afterwards** is untouched by this, and
is where the route would have to go. Nothing here says such a mechanism does or
does not exist.

It is **not** a claim that `N = 5` or `N = 4` is the framework's level, nor that
any of these phases is realised. It derives an admissible *set* and observes that
the required phase is outside it. Nothing is wired; no `c_k` moves.

**A consonance, recorded and explicitly not offered as support.** `N = 5` is not
a foreign number in this corpus — Bring's curve, `S₅`/`A₅`, the binary
icosahedral `2I`, the `s5-so3` keystone. That is consonance, not evidence, and
this corpus has documented precedent for mistaking one for the other (the stale
`−2.00973976` / `J_Hopf − ħ_q²` agreement). **No search was run on it**, and none
should be until something independent selects a level.
