| Quantity at $q_0 = 1.109978595557335$ | Value |
|---|---|
| $h = q - q^{-1}$ | $0.2090603219955937$ |
| $z = 1/(\sqrt q + 1/\sqrt q)$ | $0.4993203340335613$ |
| Form A: $\lvert\Delta(\mathrm{net})\rvert$ | $0.187207212879143$ |
| Form B: $\ln(1 + z h)$ | $0.09929139859972778$ |
| Predicted bridge $1/z + (z-1)h/(2z)$ | $1.897907634269324$ |
| Actual bridge $\mathrm{A}/\mathrm{B}$ | $1.885432328673596$ |
| Residual $\lvert$predicted $-$ actual$\rvert$ | $0.0124753$ |
| $O(h^2)$ tolerance ($h^2$) | $0.04370621823290131$ |
| $\mathfrak{Q}_\beta^{\mathrm{A}} = \lvert\Delta(\mathrm{net})\rvert \cdot E_0$ | $0.783645803897$ MeV |
| $\mathfrak{Q}_\beta^{\mathrm{B}} = \ln(1+zh) \cdot E_0 / z$ | $0.832395283254$ MeV |
| $\lvert \mathfrak{Q}_\beta^{\mathrm{A}} - \mathfrak{Q}_\beta^{\mathrm{B}}\rvert$ | $0.0487495$ MeV ($< h^2 E_0 = 0.183$ MeV) |

> **⚠ The provenance sentence that stood here was false, and the divergence it
> hid is 21 %** (measured 2026-09-05, `qou-i229`). It read: *"Values are the
> displayed digits of the 50-dps witness `q-beta-spectral-bridge.witness.json`,
> regenerated from the canonical CAL-2 pinning `q-pinning-50-digit.witness.json`."*
> The witness contains **none** of these values and declares
> `q0Anchor: proton`, not the canonical CAL-2 (muon) pinning.
>
> | | this table | the witness |
> |---|---|---|
> | $q_0$ | $1.109978595557335$ | $1.1099785827513808\ldots$ (proton) |
> | $z$ | $0.4993203340335613$ | $0.6126880371464652\ldots$ |
> | $\ln(1+zh)$ | $0.09929139859972778$ | $0.1205248238414840\ldots$ |
> | predicted bridge | $1.897907634269324$ | $1.5660730493910099\ldots$ |
>
> Each side reproduces its own numbers exactly, so this is **two different
> computations**, not drift: the bridge ratio differs by $21.2\,\%$.
>
> **This table matches its own proposition and the producer does not.**
> [`prop:q-beta-spectral-bridge`](#prop:q-beta-spectral-bridge) *defines*
> $z := 1/(\sqrt q + 1/\sqrt q)$, which is what these values use;
> `q_beta_spectral_bridge_witness.py` computes $q^3/(q^2+1)$ instead — and
> stores it under the field name `z_markov_jones`, while the proposition calls
> *its* $z$ "the Markov–Jones parameter". **The same name for two formulas is
> what hid this**, and both of the witness's assertions PASS, because a producer
> checking itself against itself cannot see that it has drifted from the block
> it names in `contentBlock`.
>
> Which $z$ is right is an authoring question and is **not** settled here; the
> $\mathfrak{Q}_\beta$ figures differ by $\sim 0.05$ MeV between the two
> readings. Nothing in this table, the proposition or the producer has been
> changed — only this sentence, which was false under either reading.
> `the_qbeta_bridge_table_and_its_witness_compute_different_z_probe.py`.

> **⚠ Retraction (2026-09-05).** A caveat here said $h^2 = 0.04370621823290131$
> "carries a retired $q_0$" and that this table was internally inconsistent.
> **Both are withdrawn.** $h^2$ is exactly $(h)^2$ as published — they agree to
> $9.0\times10^{-18}$ — and every value in the table reproduces from the quoted
> $q_0$ with the proposition's own $z$. The earlier claim came from matching
> $h^2$ against closed forms at three candidate pins, where the significant-figure
> bucketing was too coarse to separate them. The table is self-consistent; what
> is not is its relationship to the producer, above.
