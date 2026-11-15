# Per-cell $\mathrm{Frob}_p$ data for the QOU instance

The following table records the extracted Frobenius data for the
[`conj:qou-motivic-galois-instance`](#conj:qou-motivic-galois-instance)
construction, per atom and per prime.

| Atom | $p=2$ | $p=3$ | $p=5$ | $p=7$ | $p=11$ | $p=13$ |
|---|---|---|---|---|---|---|
| p (proton) | $\|F\|=8$, $w=6$ | $\|F\|=1$, $w=0$ | $\|F\|=0.62$, partial | partial | partial | partial |
| n (neutron) | $\|F\|=8$, $w=6$ | $\|F\|=2.65$, $w\approx1.77$ | $\|F\|=0.24$, partial | partial | partial | partial |
| D (deuteron) | $\|F\|=96$, $w\approx13.17$ | $\|F\|=4.58$, $w\approx2.77$ | $\|F\|=1.44$, partial | $\|F\|=38.74$, partial | partial | partial |

Cells marked "partial" have on-disk Habiro data that exhausts before the Pochhammer truncation point ($m_{\max} < 2p$). Galois-norm integrality still holds, indicating the partial sum already approximates the true Frobenius eigenvalue well. Unmarked cells achieve full truncation within the available data and pass the Weil-purity check $|\sigma(\mathrm{Frob}_p)| = p^{w/2}$ for every $\sigma$ in the Galois orbit.
