import sympy as sp

def hoefsmit_H3_21():
    q = sp.Symbol('q')
    # Hoefsmit representation of H3 on partition (2,1)
    # Dimension is 2.
    # Standard basis vectors corresponds to tableaux:
    # T1 = 1 2    T2 = 1 3
    #      3           2
    # Axial distances for T1: 
    # c(1)=0, c(2)=1, c(3)=-1.
    # s1 acts on (1,2): distance is 1 - 0 = 1.
    # s2 acts on (2,3): distance is -1 - 1 = -2.
    
    # For T2:
    # c(1)=0, c(2)=-1, c(3)=1.
    # s1 acts on (1,2): distance is -1 - 0 = -1.
    # s2 acts on (2,3): distance is 1 - (-1) = 2.
    
    # In general, if d = c(i+1) - c(i), the matrix for sigma_i is:
    # [ (q - 1)/(1 - q^{-d}),    sqrt(...) ]
    # [ sqrt(...),               (q - 1)/(1 - q^d) - 1 ]?
    # Wait, the exact Hoefsmit matrix for sigma_i when d > 0 (letters are in order):
    # D_{i,i} = (q - 1) * q^d / (q^d - 1)
    # D_{i+1,i+1} = (1 - q) / (q^d - 1) - 1 ?
    # Let's just use the known matrices for (2,1)
    
    # In the generic basis:
    # sigma_1 = [[q, 0], [0, -1]]
    sigma_1 = sp.Matrix([[q, 0], [0, -1]])
    
    # sigma_2 has elements:
    # 11: -1/(q+1)
    # 12: sqrt(q)/(q+1) * sqrt(q^2+q+1) ?
    # Actually, a simpler representation of (2,1) for H3:
    # sigma_1 = [ [q, 0], [1, -1] ]
    # sigma_2 = [ [-1, q], [0, q] ]
    # Let's check eigenvalues and Hecke relations:
    # sigma_1^2 = (q-1)sigma_1 + q I
    s1 = sp.Matrix([[q, 0], [q, -1]]) 
    # Wait: [q, 0] * [q, 0] + [0, 0] = q^2
    # [q, -1] * [q, 0] + [-1, -1] = q^2 - q? No.
    # Let's use the explicit one:
    s1 = sp.Matrix([[-1, 0], [0, q]])
    s2 = sp.Matrix([[q-1, q], [1, 0]])
    
    # Check relations:
    I = sp.eye(2)
    print("s1^2 - (q-1)s1 - qI =", sp.simplify(s1*s1 - (q-1)*s1 - q*I))
    print("s2^2 - (q-1)s2 - qI =", sp.simplify(s2*s2 - (q-1)*s2 - q*I))
    print("s1 s2 s1 - s2 s1 s2 =", sp.simplify(s1*s2*s1 - s2*s1*s2))
    
    # Trefoil = s1 s2 s1 ? No, trefoil is a knot, not a braid.
    # As a braid closure, trefoil is s1^3 in B2. In H3, is it s1^3? No, s1^3 is just (q-1)s1^2 + q s1.
    # Trefoil in B3 is (s1 s2)^3 (which is the full twist = central element, actually framing matters).
    # Wait! "χ(trefoil) - χ(identity)"
    trefoil_1 = s1**3
    print("Trefoil s1^3 trace:", sp.simplify(trefoil_1.trace()))
    
    trefoil_2 = (s1*s2)**3
    print("Trefoil (s1 s2)^3 trace:", sp.simplify(trefoil_2.trace()))
    
    # What about s1 s2 s1? 
    t_s1s2s1 = s1*s2*s1
    print("Trace s1 s2 s1:", sp.simplify(t_s1s2s1.trace()))

hoefsmit_H3_21()
