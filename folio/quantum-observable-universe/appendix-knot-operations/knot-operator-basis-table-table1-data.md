**Table L.1 — normal-form (NF) basis multiplication.** This table
records the raw product $b_i \cdot b_j$ of the NF basis operators —
the case of the identity operator $\beta(T_{1,0}) = \mathbf{1}$ —
re-expanded in the same basis. Reading the row $b_i$ against the
column $b_j$ gives the coefficient of that column operator in the
product $b_i \cdot b_j$; every entry is exact in $h$, and "—" marks a
vanishing coefficient.

**Notation.** $h = q - q^{-1}$ (Hecke amplitude). The NF basis is
$\{\ \gamma,\ \sigma_0,\ \sigma_1,\ L_+,\ L_-,\ e^-\ \}$, with
$e^- = \sigma_0\sigma_1\sigma_0$ (the electron word; its closure on three strands is the Hopf link). The operator $\gamma$
is the two-sided identity: $\gamma \cdot b_j = b_j$ and
$b_i \cdot \gamma = b_i$. The identity rows below (the header row
$\gamma \cdot b_j$ and the right-multiply rows $b_i \cdot \gamma$)
therefore list the single surviving operator directly and leave the
remaining cells empty.

| $b_i \cdot b_j$ | $\gamma$ | $\sigma_0$ | $\sigma_1$ | $L_+$ | $L_-$ | $e^-$ |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| $\gamma \cdot b_j$ | $\gamma$ | $\sigma_0$ | $\sigma_1$ | $L_+$ | $L_-$ | $e^-$ |
| $\sigma_0 \cdot \gamma$ | $\sigma_0$ | | | | | |
| $\sigma_0 \cdot \sigma_0$ | $1$ | $h$ | — | — | — | — |
| $\sigma_0 \cdot \sigma_1$ | — | — | — | $1$ | — | — |
| $\sigma_0 \cdot L_+$ | — | — | $1$ | $h$ | — | — |
| $\sigma_0 \cdot L_-$ | — | — | — | — | — | $1$ |
| $\sigma_0 \cdot e^-$ | — | — | — | — | $1$ | $h$ |
| $\sigma_1 \cdot \gamma$ | $\sigma_1$ | | | | | |
| $\sigma_1 \cdot \sigma_0$ | — | — | — | — | $1$ | — |
| $\sigma_1 \cdot \sigma_1$ | $1$ | — | $h$ | — | — | — |
| $\sigma_1 \cdot L_+$ | — | — | — | — | — | $1$ |
| $\sigma_1 \cdot L_-$ | — | $1$ | — | — | $h$ | — |
| $\sigma_1 \cdot e^-$ | — | — | — | $1$ | — | $h$ |
| $L_+ \cdot \gamma$ | $L_+$ | | | | | |
| $L_+ \cdot \sigma_0$ | — | — | — | — | — | $1$ |
| $L_+ \cdot \sigma_1$ | — | $1$ | — | $h$ | — | — |
| $L_+ \cdot L_+$ | — | — | — | — | $1$ | $h$ |
| $L_+ \cdot L_-$ | $1$ | $h$ | — | — | — | $h$ |
| $L_+ \cdot e^-$ | — | — | $1$ | $h$ | $h$ | $h^2$ |
| $L_- \cdot \gamma$ | $L_-$ | | | | | |
| $L_- \cdot \sigma_0$ | — | — | $1$ | — | $h$ | — |
| $L_- \cdot \sigma_1$ | — | — | — | — | — | $1$ |
| $L_- \cdot L_+$ | $1$ | — | $h$ | — | — | $h$ |
| $L_- \cdot L_-$ | — | — | — | $1$ | — | $h$ |
| $L_- \cdot e^-$ | — | $1$ | — | $h$ | $h$ | $h^2$ |
| $e^- \cdot \gamma$ | $e^-$ | | | | | |
| $e^- \cdot \sigma_0$ | — | — | — | $1$ | — | $h$ |
| $e^- \cdot \sigma_1$ | — | — | — | — | $1$ | $h$ |
| $e^- \cdot L_+$ | — | $1$ | — | $h$ | $h$ | $h^2$ |
| $e^- \cdot L_-$ | — | — | $1$ | $h$ | $h$ | $h^2$ |
| $e^- \cdot e^-$ | $1$ | $h$ | $h$ | $h^2$ | $h^2$ | $h^3+h$ |
