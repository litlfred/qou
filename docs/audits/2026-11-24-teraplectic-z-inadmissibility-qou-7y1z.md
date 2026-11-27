# Teraplectic $z = 0.99850030$ Is Not an Admissible Markov Parameter Under Convention D (`qou-7y1z`)

**Date:** 2026-11-24  
**Bean:** `qou-7y1z` (parent epic `qou-wxhi` / `qou-cds1`)  
**Companion D-Ladder Audit:** [`2026-09-12-zd-gap-anatomy-and-three-undone-migrations.md`](2026-09-12-zd-gap-anatomy-and-three-undone-migrations.md) §2b  
**Probe & 80-dps Witness:** [`computations/probes/teraplectic_z_inadmissibility_80dps_probe.py`](../../computations/probes/teraplectic_z_inadmissibility_80dps_probe.py) $\to$ [`computations/probes/teraplectic-z-inadmissibility-80dps.witness.json`](../../computations/probes/teraplectic-z-inadmissibility-80dps.witness.json) (`5/5` assertions passed at `compute_dps = 95`, `output_dps = 80`, proton pin `q_at(95)`)

---

## 1. Claim & Exclusion Ruling

The teraplectic / inverse-solved Markov parameter candidate $z_{\mathrm{tera}} = 0.99850030$ (along with the exact affine-base inverse roots $z^\star_{\mathrm{ord0}} = 0.99850030362278\ldots$ and $z^\star_{\mathrm{tower}} = 0.99124653789861\ldots$ solving $|\tfrac{1}{2}h_0^2 - z\,h_0|\,\mathfrak{E}_0 = \mathfrak{Q}_\beta^{\mathrm{CODATA}}$) **must not be used** in any Convention-D $\mathfrak{Q}_\beta$ or $c_k$-ladder derivation:

1. **Disjoint from the two-row admissible root set (`ConventionDAdmissibleRoots.lean`).** On $H_3(q_0)$, the 3-row Ocneanu Markov weight is
   $$y_{(1^3)}(z) \;=\; \frac{q_0^2\,(z - q_0)\,\bigl((q_0^2+1)z - q_0^3\bigr)}{(q_0^2+1)(q_0^4+q_0^2+1)}.$$
   Its unique roots are $z = q_0$ (the trivial 1-row augmentation character, where $y_{(2,1)}(q_0) = 0$) and $z_D = \frac{q_0^3}{q_0^2+1} = 0.61268803714646525160\ldots$ (the canonical two-row Temperley–Lieb trace). At the proton pin $q_0 = 1.10997858275138080759\ldots$:
   - $|z_{\mathrm{tera}} - q_0| = 0.11147828275138080759\ldots > 0.111$,
   - $|z_{\mathrm{tera}} - z_D| = 0.38581226285353474840\ldots > 0.385$.
2. **Violates Markov weight positivity ($y_{(1^3)} < 0$).** Because $z_D < z_{\mathrm{tera}} < q_0$, the two linear factors $(z_{\mathrm{tera}} - q_0) < 0$ and $((q_0^2+1)z_{\mathrm{tera}} - q_0^3) > 0$ have opposite signs, forcing
   $$y_{(1^3)}(z_{\mathrm{tera}}) \;=\; -0.01413069645380553577\ldots \;<\; 0.$$
   Thus $z_{\mathrm{tera}}$ is not a positive trace on $H_3(q_0)$, does not factor through $TL_3(q_0)$, and tuning $z \mapsto 0.99850030$ to match $\mathfrak{Q}_\beta^{\mathrm{CODATA}}$ on $\Delta_S$ would additionally violate the strict anti-fit discipline (`NO FITTING EXCEPT CAL-1/2/3`).

## 2. Consequence for `qou-wxhi` / `qou-cds1`

Under Convention D, $z = z_D = q_0^3/(q_0^2+1)$ is fixed. Closing the $\mathfrak{Q}_\beta$ base and $c_k$ ladder must proceed via the admissible element / representation-theoretic structure at $z = z_D$ (as tracked in `qou-wxhi` and `2026-09-12-zd-gap-anatomy-and-three-undone-migrations.md`), never by substituting $z \approx 0.99850030$.
