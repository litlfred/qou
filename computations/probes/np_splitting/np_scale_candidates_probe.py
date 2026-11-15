"""Pre-registered (written before running): which mass scale multiplies the level-2
weight-space log-ratio |ΔΦ| = 2 ln q, according to each corpus mass formula?
Candidates are fixed here; none is selected by its residual.
 S0  asserted:   Δm = α·|ΔΦ|, α = m_e·8G   (neutron-proton-mass-splitting proof, one sentence)
 S1  canonical facade, weight entering F_Bor: m = 2(m_μ F − 6 m_e), F_n/F_p = q^{±2}
 S2  linearised facade: Δm = 2 m_μ F · |ΔΦ|
 S3  unified mass formula m = m_e·Vol·ρ/ℏ_q², ρ ratio q^{±2}, Vol = 8G (Borromean)
Report all; CODATA 1.29333205 MeV is the comparison only.
"""
from mpmath import mp,mpf,log,catalan
from qou_substrate.constants import q_at  # proton pin, derived, not a typed copy
mp.dps=40
q=mpf(q_at(60))
me=mpf('0.51099895069'); mpr=mpf('938.27208816'); cod=mpf('1.29333205')
dPhi=2*log(q); a=me*8*catalan; hq=1-1/q
mmuF=mpr/2+6*me
rows={
 'S0 alpha*dPhi':a*dPhi,
 'S1 facade F*q^2 (n heavier)':2*mmuF*(q**2-1),
 'S1 facade F*q^-2':2*mmuF*(1-q**-2),
 'S2 linearised facade':2*mmuF*dPhi,
 'S3 m_e*8G/hq^2*(q^2-1)':me*8*catalan/hq**2*(q**2-1),
}
for k,v in rows.items(): print(f"{k:32s} {mp.nstr(v,10):>14s} MeV  {mp.nstr(100*(v/cod-1),6):>10s} %")
