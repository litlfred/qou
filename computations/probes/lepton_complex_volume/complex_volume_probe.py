import snappy
W={'e':[1,2,1],'mu':[1,1,1,1,-2],'tau':[1,1,-2,1,-2],'4_1':[1,-2,1,-2],'oldmu':[1,1,-2],'oldtau':[1,1,1,1,-2]}
def mirror(w): return [-x for x in w]
for k,w in W.items():
  for lab,ww in (('',w),('mirror',mirror(w))):
    out=[]
    for kind,b in (('closure',ww),('cl+axis',ww+[3,2,1,1,2,3])):
      M=snappy.Link(braid_closure=b).exterior()
      try: cv=M.complex_volume(); sol=M.solution_type()
      except Exception as ex: cv=str(ex); sol=''
      out.append(f"{kind}: {cv} [{sol[:12]}] ncusps={M.num_cusps()}")
    print(k,lab,' | '.join(out))
