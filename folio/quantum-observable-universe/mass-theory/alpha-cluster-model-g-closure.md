**Remark (Model G — a phenomenological closure interpreting the activation
gate).**

> **This is a structural/phenomenological model, not a parameter-free
> derivation.** The cluster bindings $B(\text{cluster})$ enter at their
> *measured* AME values (an input); the light-spectator coefficient
> $b = 0.78\ \mathrm{MeV}$ is calibrated empirically on three one-bond
> composites; the gated pair coefficient $g = 2.4155\ \mathrm{MeV}$ is a guarded
> near-match ($\approx 3b$, $-2.9\%$); the saturation count $\binom{k}{2}$ is
> data-selected. Model G derives the *composite structure* — **which** $\alpha
> \cdot \alpha$ pairs activate, via the proved gate
> [The $\alpha$-cluster activation gate](#prop:alpha-cluster-activation-gate) —
> **not** the absolute cluster base. It is recorded here for its structural
> content alone, and must not be cited as an ab-initio prediction.

Applying the activation gate to the light $\alpha$-conjugate (and
$\alpha + \text{light-remainder}$) isotopes, with cluster decompositions
$^6\mathrm{Li} = \alpha + d$, $^7\mathrm{Li} = \alpha + t$,
$^8\mathrm{Be} = 2\alpha$, $^9\mathrm{Be} = 2\alpha + n$, $^{12}\mathrm{C} = 3\alpha$,
$^{16}\mathrm{O} = 4\alpha$, the model reads

$$
B(\text{isotope}) \;\approx\; \sum_{\text{clusters}} B(\text{cluster})
  \;+\; b\,A_{\text{light}} \;+\; g\,\binom{k}{2}\,[\,k \ge 3\,],
$$

where $k$ is the number of $\alpha$-clusters, $A_{\text{light}}$ the
light-remainder nucleon count, and $[\,k\ge 3\,]$ the Iverson bracket for the
gated $\alpha\cdot\alpha$ pair term. The pair term is switched on only for
$k\ge 3$ — the gate's Hopf-spectator closure (part 1 of the proposition)
suppresses the $k=2$ ($^8\mathrm{Be}$) pair, while a Borromean triple of
$\alpha$-clusters (part 2) opens it.

**Residuals** (percent of $B_{\mathrm{AME}}$; $^{12}\mathrm{C}$ and
$^{16}\mathrm{O}$ are out-of-sample, constants fixed before evaluation):

| isotope | clusters | residual |
|---|---|---|
| $^6\mathrm{Li}$ | $\alpha + d$ | $+0.28\%$ |
| $^7\mathrm{Li}$ | $\alpha + t$ | $-0.31\%$ |
| $^8\mathrm{Be}$ | $2\alpha$ | $+0.16\%$ |
| $^9\mathrm{Be}$ | $2\alpha + n$ | $-0.02\%$ |
| $^{12}\mathrm{C}$ | $3\alpha$ | $-0.26\%$ |
| $^{16}\mathrm{O}$ | $4\alpha$ | $-0.28\%$ |

**Epistemic tiers of the ingredients** (the proved gate vs. the fitted
closure):

| ingredient | tier |
|---|---|
| bond-count multiplicity $M_n = n-1$ | proved ([linear-chain bond count](#prop:linear-chain-bond-count)) |
| $\bar\mu$ sign-rep obstruction (coupling through $\lvert\bar\mu\rvert$ only) | proved |
| Milnor-indeterminacy gate (Hopf spectator $\Rightarrow$ inactive; $\alpha$-only activation) | proved (+ literature `milnor1954`) |
| W-plane annihilation on $\mathrm{Vol}=0$ bond channels | proved |
| CAL-3 bond-channel class selection | conditional (on an open binding-volume ledger hypothesis) |
| $\alpha\cdot\alpha$ activation applied to specific isotopes ($^8\mathrm{Be}\approx 0$, $k\ge 3$) | conditional on the Brunnian arrangement model |
| $b = 0.78\ \mathrm{MeV/nucleon}$ | **empirical** (calibrated on 3 one-bond composites) |
| $\binom{k}{2}$ saturation counting | **data-selected** |
| $g = 2.4155 \approx 3b$ ($-2.9\%$) | **guarded near-match** |
| $^{11}\mathrm{B} / {}^{14}\mathrm{N} / {}^{19}\mathrm{F}$ mixed multi-bond | **open** ($-58/-33/-10\%$ deficit) |

Numerical verification (checks only; no result elsewhere in this paper
depends on them):
[Brunnian activation check](../../../computations/deltalambda/alpha-activation-brunnian.witness.json)
(9/9), building on
[cluster volume-additivity check](../../../computations/deltalambda/alpha-cluster-volume-additivity.witness.json)
(7/7) and
[inter-cluster bond-term check](../../../computations/deltalambda/inter-cluster-bond-term.witness.json)
(10/10). The ab-initio route for the cluster bases (replacing the AME input) is
the separate bond-count tower — $^3\mathrm{H}$ to $\approx 0.16\%$ with no fit;
$^4\mathrm{He}$ remains open (the $\mathrm{Vol}_4$ census gap).
