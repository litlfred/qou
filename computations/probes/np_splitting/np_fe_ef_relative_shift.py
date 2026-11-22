# Dimensionless relative shift (t_n - t_p)/T_full for X in {1, FE, EF} on V^3 (audit §20 addendum; asked by Bridge B).
# Runs the pre-registered FE/EF probe and reuses its definitions. Exact sympy; display via mpmath.
import runpy,sys,io,contextlib
f=io.StringIO()
with contextlib.redirect_stdout(f):
    g=runpy.run_path('computations/probes/np_splitting/np_second_order_weak_fe_ef_probe.py')
sp=g['sp'];q=g['q'];t=g['t'];V=g['V'];F=g['F'];E=g['E'];num=g['num'];mp=g['mp']
for xn,X in (('1',sp.eye(8)),('FE',F*E),('EF',E*F)):
    W=X*V**3
    tp,tn=t(W,(0,0,1)),t(W,(0,1,1))
    full=sum(t(W,w) for w in [(0,0,0),(0,0,1),(0,1,1),(1,1,1)])
    print(xn,'t_p',mp.nstr(num(tp),10),'t_n',mp.nstr(num(tn),10),'T_full',mp.nstr(num(full),10),'(t_n-t_p)/T_full',mp.nstr(num((tn-tp)/full),8), ' at q=1:', sp.simplify(((tn-tp)/full).subs(q,1)))
