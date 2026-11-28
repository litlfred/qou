**(a) Photonic, four-photon, and $A = 1$ single-hadron $H_3(q_0)$ normal forms and LP-dual shadow invariants** (all rows carry full-Wedderburn radical shadow coordinate $u_{(1,1,1)}^* = \text{null}$ on $[0, +\infty)$ and $6 \times 6$ NF-Gram net shadow price $y_0^{*,\mathrm{NF}} = 0$):

| Channel / State | $H_3(q_0)$ Normal Form $[c_{\mathbf{1}}, c_{\sigma_0}, c_{\sigma_1}, c_{L_+}, c_{L_-}, c_{e^-}]$ | $\operatorname{tr}_M(W)$ | $\operatorname{net}(W)$ | $U(1)$ Neutral | $\min_{\lambda \vdash_2 3} \frac{\chi^\lambda}{\dim\lambda}$ | Reading 3 ($m = 1..3$) | $y_0^{*,\mathrm{quot}}$ | $(u_{(3)}^{*,\mathrm{quot}}, u_{(2,1)}^{*,\mathrm{quot}})$ | Status |
|---|---|---:|---:|---|---:|---|---:|---|---|
| $\gamma(0,0,0) = \mathbf{1}$ | `[1, 0, 0, 0, 0, 0]` | `1.000000000000` | `1.000000000000` | Yes (`3`-unlink) | `+1.000000000` | Pass | `0.494595773` | `(0.021386, 0)` | Theorem |
| $\gamma_+ = \gamma(0,0,q_0 h_{\mathrm{A}})$ | `[1, -0.04851296, 0, +0.23205245, 0, 0]` | `1.057386081530` | `1.183539498762` | Yes (termwise) | `+0.878902706` | Pass | `0.434701564` | `(0.301891, 0)` | Theorem |
| $\gamma_- = \gamma(0,0,-q_0^{-1}h_{\mathrm{A}})$ | `[1, +0.03937572, 0, -0.18834625, 0, 0]` | `0.953422371478` | `0.851029476755` | Yes (termwise) | `+0.811653754` | Pass | `0.410213238` | `(0, 0.244834)` | Theorem |
| $V = \sigma_0\sigma_1^{-1}$ | `[0, -0.20906030, 0, +1, 0, 0]` | `0.247297886748` | `0.790939701204` | Yes ($0_1$ knot) | `-0.521853104` | Fail | `0.258106340` | `(0.489307, 0)` | Theorem |
| $V^2 = (\sigma_0\sigma_1^{-1})^2$ | `[+0.04370621, +0.00913723, -0.20906030, -0.04370621, +1, 0]` | `0.280195642273` | `0.800076934219` | Yes ($4_1$ knot) | `-0.455338675` | Fail | `0.225208584` | `(0.554399, 0)` | Theorem |
| $\beta_{\mathrm{Bor}} = V^3 = \gamma_+\gamma_-$ | `[+0.99808977, -0.00953659, +0.00913723, +0.04561644, -0.04370621, 0]` | `0.998562163837` | `0.999600646188` | Yes ($\operatorname{lk}=0$) | `+0.997092906` | Pass | `0.493157937` | `(0.024231, 0)` | Theorem |
| $(\gamma_+\gamma_-)^2 = V^6$ | `[+0.99237018, -0.01941708, +0.01782199, +0.09287789, -0.08524807, 0]` | `0.994257015196` | `0.998404906671` | Yes ($\operatorname{lk}=0$) | `+0.988388528` | Pass | `0.488852789` | `(0.032749, 0)` | Theorem |
| $\gamma_+^4 = (1 + q_0 h_{\mathrm{A}} V)^4$ | `[+1.0638872, -0.19218017, -0.06711625, +0.91925713, +0.32103777, 0]` | `1.370609477795` | `2.044885646647` | Yes (termwise) | `+0.416635428` | Pass | `0.206066122` | `(0.823050, 0)` | Theorem |
| $\gamma_-^4 = (1 - q_0^{-1} h_{\mathrm{A}} V)^4$ | `[+0.98257543, +0.15944052, -0.04475382, -0.76265329, +0.21407134, 0]` | `0.846912276958` | `0.548680189182` | Yes (termwise) | `+0.433993482` | Pass | `0.219342140` | `(0, 0.650490)` | Theorem |
| $\pi^\pm = \sigma_0^2$ | `[1, +0.20906030, 0, 0, 0, 0]` | `1.128088744114` | `1.209060298796` | No ($\operatorname{lk}=+1$) | `+1.021853104` | Pass | `0.505404227` | `(0.188346, 0)` | Conditional |
| $\mathfrak{p}$ (`uud`, 11-letter) | `[-0.09218805, +0.01645655, +0.99952244, +0.09032074, +0.21829737, -0.02432530]` | `0.629328402203` | `1.208083750892` | No (skein) | `-0.140296675` | Fail | `0.069390143` | `(0.900689, 0)` | Conditional |
| $\mathfrak{n}$ (`udd`, 11-letter) | `[-0.19164167, +0.00806571, +1.0109266, -0.01887786, +0.22058168, -0.04813038]` | `0.475133517156` | `0.980924039127` | No (skein) | `-0.185978162` | Fail | `0.091984013` | `(0.837804, 0)` | Conditional |

**(b) Full-strand $A = 2 \ldots 4$ ($6, 9, 12$-strand) colour-valence $\gamma\gamma$-bonded nuclear braids** ($M_{\mathrm{T3}}(A) = 3\lfloor A/2 \rfloor$; unfitted log-trace energy $B_A = -E_0^{\mathrm{tower}} \ln r_A$ at $E_0^{\mathrm{tower}} = 4.227483355629\;\mathrm{MeV}$, *Conditional*):

| Nuclide ($3A$ strands) | Nucleon Cell | Bond Graph & Transport | Bonds $M$ | $r_A = \frac{\operatorname{tr}_M(\text{bound})}{\operatorname{tr}_M(\text{free})}$ | Reading 3 ($m = 1..3A$) | $B_A^{\mathrm{tower}}$ (keV) | $B_{\mathrm{AME}}$ (MeV) | Rel. Error | Status |
|---|---|---|---:|---:|---|---:|---:|---:|---|
| ${}^2\mathrm{H}$ ($6$) | Bare $\gamma\gamma$ $V^3$ | $K_2$ pair `(0,1)` | `1` | `0.998497160633` | Pass (`+0.9915`) | `+6.358` | `2.22457` | `-99.71%` | Conditional |
| ${}^2\mathrm{H}$ ($6$) | Typed `pn` | $K_2$ pair `(0,1)` | `1` | `1.000611191407` | Fail ($m=3,4$) | `-2.583` | `2.22457` | `-100.12%` | Conditional |
| ${}^3\mathrm{H}$ ($9$) | Bare $\gamma\gamma$ $V^3$ | $K_3$ all-pairs (`over` = `under`) | `3` | `0.995581770818` | Pass (`+0.9866`) | `+18.719` | `8.48180` | `-99.78%` | Conditional |
| ${}^3\mathrm{He}$ ($9$) | Bare $\gamma\gamma$ $V^3$ | $K_3$ all-pairs (`over` = `under`) | `3` | `0.995581770818` | Pass (`+0.9866`) | `+18.719` | `7.71804` | `-99.76%` | Conditional |
| ${}^3\mathrm{H}$ ($9$) | Typed `pnn` | $K_3$ all-pairs (`over` / `under`) | `3` | `1.001859942930` | Fail ($m=3,4$) | `-7.856` | `8.48180` | `-100.09%` | Conditional |
| ${}^3\mathrm{He}$ ($9$) | Typed `ppn` | $K_3$ all-pairs (`over` / `under`) | `3` | `1.002320256701` | Fail ($m=3,4$) | `-9.797` | `7.71804` | `-100.13%` | Conditional |
| ${}^4\mathrm{He}$ ($12$) | Bare $\gamma\gamma$ $V^3$ | $K_4$ `D+D` / `3H+p` / `3He+n` (`over`) | `6` | `0.991352791820` | Pass (`+0.9792`) | `+36.715` | `28.29567` | `-99.87%` | Conditional |
| ${}^4\mathrm{He}$ ($12$) | Bare $\gamma\gamma$ $V^3$ | $K_4$ `D+D` / `3H+p` / `3He+n` (`under`) | `6` | `0.991350330312` | Pass (`+0.9794`) | `+36.725` | `28.29567` | `-99.87%` | Conditional |
| ${}^4\mathrm{He}$ ($12$) | Bare $\gamma\gamma$ $V^3$ | $K_4$ Tait 3-edge-coloured (`over`) | `6` | `0.991516901932` | Pass (`+0.9802`) | `+36.015` | `28.29567` | `-99.87%` | Conditional |
| ${}^4\mathrm{He}$ ($12$) | Typed `ppnn` | $K_4$ `D+D` pairing a (`over`) | `6` | `1.004251409825` | Fail ($m=3,4$) | `-17.935` | `28.29567` | `-100.06%` | Conditional |

**(c) Exploratory multi-strand $\gamma\gamma$ channels** (*Exploratory / Unselected* — reported without target selection):

| Exploratory Channel | Strand & Vertex Census | Passing Words / Pairs | Representative Word & Algebraic Reduction | $\operatorname{tr}_M(W)$ or $r_A$ Range | Reading 3 Verdict | Unfitted Observable Range | Status |
|---|---|---|---|---|---|---|---|
| $H_4(q_0)$ flavoured nucleon census | $n = 4$, $L \le 6$ in $\{V_0, V_1\}$ (`126` words) | `12` single-nucleon words | $V_0^3$, $V_1^3$ ($L=3$); $V_0 V_1 V_0 V_1$, $V_1 V_0 V_1 V_0$ ($L=4$); `8` words at $L=6$ | $\operatorname{tr}_M \in [0.994257, 1.032898]$; $E_{4\to 3}(z)$ $\operatorname{net} \in [0.988547, 1.107037]$ | `12 / 126` pass ($m = 1..4$) | Production targets $\operatorname{net}(\mathfrak{p}) = 0.895470$, $\operatorname{net}(\mathfrak{n}) = 0.708263$ | Exploratory / Unselected |
| $H_8(q_0)$ flavoured deuteron pairs | $n = 8$, $12^2$ pairs $\times$ $6$ bonds $V(3)^k, V(2)^k$ | `288 / 864` (`144` with $V(3)^3$, `282` bound) | $(V_0^3, V_0^3) \cdot V(3)^3$ ($r = 0.998497160633$) to $(V_0^3, V_0^6) \cdot V(3)^3$ | $r \in [0.998419657, 1.000000000]$ | `288 / 864` pass ($m = 1..8$) | $B^{\mathrm{tower}} \in [-7.9 \times 10^{-93},\, +6.686]\;\mathrm{keV}$ | Exploratory / Unselected |
| $H_6(q_0)$ neutral lepton-pair words | $n = 6$, $L \le 5$ in $\{V_0..V_3\}$ (`1,364` words) | `60` $e^-\bar\nu_e \sqcup 0_1^2$ (`25` no-idle) + `60` $e^+\nu_e \sqcup 0_1^2$ | $V_0 V_1 V_2 V_0 V_3 = \sigma_0^2 \sigma_1^{-1} \sigma_4^{-1} = h_{\mathrm{A}}^2 \gamma_0(0, -h_{\mathrm{A}}^{-1}, -1)\,\gamma_3(0, -h_{\mathrm{A}}^{-1}, 0)$ | $\operatorname{tr}_M = 0.183782973894$ (all `60`); $f_L = 0.022775205$ ($V_0 V_1 V_2 V_0 V_3$) | `4 / 60` pass ($m = 1..6$); canonical min char `-0.172453` | Framed link invariant $J_{\mathrm{framed}}/[2]_{q_0}^4 = 0.743164353$ | Exploratory / Unselected |
