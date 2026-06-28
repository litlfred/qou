# Generator Volume Decomposition Probe

## Computational verification

| Nucleus | $A$ | $\binom{A}{2}$ | $E(\mathrm{parent})$ | $E(\mathrm{daughter})$ | $\Delta E$ |
|---------|-----|:-:|---------------------|----------------------|-----------|
| ${}^{2}\mathrm{H}$ | 2 | 1 | $1.174$ | $1.000$ | $-0.174$ |
| ${}^{3}\mathrm{H}$ | 3 | 3 | $2.728$ | $2.466$ | $-0.263$ |
| ${}^{4}\mathrm{He}$ | 4 | 6 | $4.136$ | $3.794$ | $-0.342$ |
| ${}^{6}\mathrm{Li}$ | 6 | 15 | $8.054$ | $7.567$ | $-0.486$ |
| ${}^{14}\mathrm{C}$ | 14 | 91 | $47.171$ | $43.810$ | $-3.361$ |
| ${}^{60}\mathrm{Co}$ | 60 | 1770 | $38{,}863$ | $35{,}813$ | $-3{,}050$ |
| ${}^{210}\mathrm{Bi}$ | 210 | 21945 | $8.25 \times 10^{13}$ | $7.62 \times 10^{13}$ | $-6.24 \times 10^{12}$ |

All $\Delta E$ are negative — the daughter has lower energy.
The computation requires exactly $\binom{A}{2}$ transfer matrix
multiplications (including ${}^{210}\mathrm{Bi}$: 21,945 steps,
instant).

## Generator volume profile: ${}^{14}\mathrm{C}$ vs ${}^{14}\mathrm{N}$

Generators $\sigma_7$ through $\sigma_{12}$ have **identical
volumes** in both nuclei — only generators $\sigma_0$ through
$\sigma_6$ differ (the 1-jet support of the single beta decay).

| Generator | $k_i$ | $V_i({}^{14}\mathrm{C})$ | $V_i({}^{14}\mathrm{N})$ | $\Delta V_i$ |
|:---------:|:---:|:-----------------------:|:-----------------------:|:------------:|
| $\sigma_0$ | 13 | $5.970$ | $5.616$ | $-0.354$ |
| $\sigma_1$ | 12 | $5.485$ | $5.150$ | $-0.335$ |
| $\sigma_2$ | 11 | $4.823$ | $4.540$ | $-0.283$ |
| $\sigma_3$ | 10 | $4.476$ | $4.201$ | $-0.275$ |
| $\sigma_4$ | 9 | $3.887$ | $3.661$ | $-0.226$ |
| $\sigma_5$ | 8 | $3.664$ | $3.436$ | $-0.228$ |
| $\sigma_6$ | 7 | $4.603$ | $2.943$ | $-\mathbf{1.660}$ |
| $\sigma_7$--$\sigma_{12}$ | 6--1 | identical | identical | $0$ |

Generator $\sigma_6$ — the converting neutron's own generator —
has the **largest volume change** ($-1.660$, nearly half the total
$\Delta E$).  Its color degree is $k_6 = 7$: it sees 7 crossings
with downstream nucleons, ALL of which change type when the
neutron converts to a proton.  This is the highest color degree
at the converting position.
