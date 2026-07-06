def rsk(w):
    P = []
    Q = []
    for i, x in enumerate(w):
        r = 0
        while r < len(P):
            idx = -1
            for c in range(len(P[r])):
                if P[r][c] > x:
                    idx = c
                    break
            if idx == -1:
                P[r].append(x)
                Q[r].append(i + 1)
                break
            else:
                x, P[r][idx] = P[r][idx], x
                r += 1
        if r == len(P):
            P.append([x])
            Q.append([i + 1])
    return tuple(len(row) for row in P), tuple(tuple(row) for row in Q)

def canonical_Q(lam):
    Q = []
    val = 1
    for r in lam:
        row = []
        for _ in range(r):
            row.append(val)
            val += 1
        Q.append(row)
    return tuple(tuple(row) for row in Q)

def reverse_insert(P, r, x):
    row = P[r]
    idx = -1
    for i in range(len(row) - 1, -1, -1):
        if row[i] < x:
            idx = i
            break
    if idx == -1:
        raise ValueError("Invalid P tableau")
    y = row[idx]
    row[idx] = x
    return y

def inverse_rsk(P_in, Q_in):
    P = [list(row) for row in P_in]
    Q = [list(row) for row in Q_in]
    n = sum(len(row) for row in P)
    perm = []
    
    for k in range(n, 0, -1):
        r_k, c_k = -1, -1
        for i, row in enumerate(Q):
            if row and row[-1] == k:
                r_k, c_k = i, len(row) - 1
                break
        
        if r_k == -1:
            raise ValueError(f"Could not find {k} in Q")
            
        Q[r_k].pop()
        if not Q[r_k]:
            Q.pop(r_k)
            
        x = P[r_k].pop()
        if not P[r_k]:
            P.pop(r_k)
            
        for r in range(r_k - 1, -1, -1):
            x = reverse_insert(P, r, x)
            
        perm.append(x)
        
    return tuple(reversed(perm))

def generate_syt(shape):
    def get_inner_corners(curr_shape):
        corners = []
        for i in range(len(curr_shape)):
            if i == len(curr_shape) - 1 or curr_shape[i] > curr_shape[i+1]:
                corners.append((i, curr_shape[i] - 1))
        return corners

    def backtrack(curr_shape, k):
        if k == 0:
            yield {}
            return
            
        for r, c in get_inner_corners(curr_shape):
            next_shape = list(curr_shape)
            next_shape[r] -= 1
            if next_shape[r] == 0:
                next_shape.pop(r)
            next_shape = tuple(next_shape)
            
            for tab in backtrack(next_shape, k - 1):
                new_tab = tab.copy()
                new_tab[(r, c)] = k
                yield new_tab

    n = sum(shape)
    for pos_map in backtrack(shape, n):
        tab = []
        for r, l in enumerate(shape):
            row = []
            for c in range(l):
                row.append(pos_map[(r, c)])
            tab.append(tuple(row))
        yield tuple(tab)
