# 2026-07-07 Audit: FMap Algebraic Root Matching & Hexagon Projection

## Executive Summary
This audit documents the findings from the `probe_algebraic_root_matching.py` investigation into the mapping between the full Markov trace difference $\Delta\text{tr}_M(q)$ and the precision ladder variable $u_{\text{lad}}$. 

The candidate FMap $c_k$ extraction algorithm was rigorously tested against the Habiro bar-parity constraints and the Hexagon Character $V_{(2,1)}$ projection.

## 1. The Ratio Obstruction (Scalar Division Fails)
We evaluated the symbolic $w$-series expansion ($w = q-1$) of the ratio:
$$ \frac{\Delta\text{tr}_M}{\chi_{(2,1)}} = 1 + \frac{4}{5}w - \frac{41}{20}w^2 + \frac{7}{20}w^3 + \dots $$

**Finding:** The ratio contains **odd powers of $w$**. The target precision ladder sequence is constructed purely in $u_{\text{lad}} \sim w^2$, meaning it carries strictly even parity. 

This proves that the mapping from the cyclotomic topological trace to the physical observables **cannot be a simple scalar division**. The alternating parity channels identified in the cherry-picked `ZBarParity.lean` must be structurally routed.

## 2. Hexagon Projection & Categorical FMap
To construct a valid $c_k$ ladder, the framework must project out the Hexagon character $\chi_{(2,1)}$ dynamically and algebraically extract the roots $(1 + c_k u^k)$ order-by-order from the even-parity channel.

### Current Implementation Status
- **Structural Scaffolding (Proved/Wired):** The structural constraints are fully codified in Lean (`FMapDirectCyclotomic.lean` and `FMapHexagonCharacter.lean`). 
- **$N=2$ Rung (Derived):** The baseline $c_2 = -1$ (recovering the `Q_N2 = 1279 ppb` floor) correctly survives the parity projection.
- **Higher Rungs (Blocked):** The algorithmic Lean extraction for $c_3, c_4 \dots$ is currently `sorry`'d out. The empirical "best fit" $c_3 = -2$ forms are zeroed out as they fail cross-anchor rigidity (e.g. at the muon anchor).

## 3. Path to Closure
To remove the `sorry`s from the FMap scaffolds, the $q$-difference Habiro extraction logic must be explicitly solved in Lean, isolating the symmetric/even trace components that couple to the physical mass scale without bleeding into the virtual odd-parity channels.
