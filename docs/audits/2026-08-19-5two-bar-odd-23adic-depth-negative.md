# The √−23 line is special in direction, not in size — a scope-(a) negative on the bar-odd channel

**Date:** 2026-08-19 · **Axis:** c₃ / Q_β bar-odd / 5₂ · **Tier:** scope-(a)
negative, measured on 24 orders · **Discipline:** no fit, no value computed,
nothing wired, no tier change.

## The question

The corpus establishes that the 5₂ bar-odd projection lands on the √−23 line of
the trace field:

$$
P_k^{\sigma_1} - P_k^{\sigma_2} \in \sqrt{-23}\cdot\mathbb{R}\text{-axis of } K \otimes \mathbb{C}
$$

([`qbeta_5two_gswz_saddle_arithmeticity_probe.py`](../../computations/probes/qbeta_5two_gswz_saddle_arithmeticity_probe.py) §4).

That is a statement about **direction**. The natural follow-up, and the one this
audit answers, is whether the odd channel is also **arithmetically simpler** than
the element it came from. If it were, that would be a real lever: a bar-odd
closed form would carry shallower denominators than the full series, and would be
correspondingly easier to identify.

## The measurement

Writing the $k$-th element as $a_k + b_k\xi + c_k\xi^{2}$ and using $e_1 = 2$ so
that $\xi_1 + \bar\xi_1 = 2 - \xi_3$, the odd projection is

$$
\mathrm{odd}_k = (\xi_1 - \bar\xi_1)\,(u_k + v_k\xi_3),
\qquad u_k = b_k + 2c_k, \quad v_k = -c_k .
$$

Compare the 23-adic depth of the odd part, $\min(v_{23}(u_k), v_{23}(v_k))$,
against the full element's, $\min(v_{23}(a_k), v_{23}(b_k), v_{23}(c_k))$, in
exact rational arithmetic.

**They are equal at all 24 available orders.** The odd part is never shallower at
any order, and the maximum deviation is zero.

## The answer

**Negative.** The √−23 line is special in direction — that is what the
arithmeticity probe establishes — but **not in size**. Projecting to the bar-odd
channel preserves 23-adic depth rather than reducing it.

This rules out one specific hope about the *shape* of a bar-odd closed form:
that restricting attention to the line would make the arithmetic easier. It does
not.

## What this does not say

It is **not** a claim that no bar-odd closed form exists — that would be a
scope-(b) exclusion and nothing here supplies the invariant one would need. No
action **value** is computed, extracted or fitted, and nothing here bears on the
c₃ swing or on $q_0$, which is permanently gated (bean `qou-eic1`).

## A methodological note worth keeping

An earlier pass over this same data read $k = 14$ and $k = 24$ as exceptions to
the agreement. That was wrong, and instructively so: it compared the valuations
**componentwise**, where $a_k$ and $c_k$ do sometimes sit one power of 23 apart.
The depth of an element is the **minimum** over its components, and under the
minimum the two agree everywhere.

The lesson generalises past this probe. A quantity defined as an extremum over
components is not tested by comparing the components — the comparison has to be
made at the level the definition operates on. Reading it the other way turns a
clean 24-of-24 into a spurious pair of exceptions and invites a search for a
pattern that is not there.

## Cross-references

- Probe: [`fivetwo_bar_odd_23adic_depth_probe.py`](../../computations/probes/fivetwo_bar_odd_23adic_depth_probe.py) (3/3, exit 0)
- The tower: [`qbeta_5two_gswz_saddle_arithmeticity_probe.py`](../../computations/probes/qbeta_5two_gswz_saddle_arithmeticity_probe.py)
- The field: [`prop:fivetwo-trace-field`](../../content/quantum-observable-universe/appendix-qvalues/fivetwo-trace-field.md)
- The line's role: [`rem:fivetwo-bar-odd-arithmetic-home`](../../content/quantum-observable-universe/appendix-qvalues/fivetwo-bar-odd-arithmetic-home.md)
- Bean: `qou-f5xq`
