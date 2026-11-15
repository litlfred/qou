---
doc_id: arxiv-1609.08719v1
doc_title: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE"
section_id: sec-020-6-selected-examples
section_title: "Selected examples"
section_number: 6
pages: 14-17
source_pdf: 1609.08719v1.pdf
source_sha256: f61ff2111e9a97f9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.807
latex_coverage_ratio: 0.966
doc_brief: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE — We use a large census of hyperbolic 3-manifolds to experimentally investigate a conjecture of Neumann regarding the Bloch Group."
---
\label{sec:lattice-examples}

We present a selection of lattices, together with the manifolds which may
be generators.  These are constructed from the \codebit{volume\_spans.csv}
and \codebit{linear\_combinations} files of our results.

Each of the following lattices are two-dimensional: each is associated
to a polynomial with two complex places. Our results contain data for
three and even four complex places, but these are harder to represent
visually. In the following graphs, one potential generator is arbitrarily
assigned to the $x$-axis, and the other to the $y$-axis.  A point at
position $(x,y)$ represents a volume $v = a \vol(g_1) + b \vol(g_2)$,
where $x = a \vol(g_1)$ and $y = b \vol g_2)$.

The gray dots indicate our predicted lattice (based on the volumes
of all manifolds associated to that invariant trace field), while the
crosses indicate manifolds we have observed: blue $+$ markers indicate
geometric volumes, while red $\times$ markers indicate exotic volumes.
The relevant volume (whether geometric or exotic) of the manifold is
the projection to $\mathbb{R}$ of the point in the lattice.

\begin{figure}[h]
  \begin{tikzpicture}[framed]
    \begin{axis}[
                 xlabel={Projection to generator $\vol(v1859(-1,3))$},
                 ylabel={Projection to generator $\vol(t07828)$},
                ]
      \addplot[color=gray, mark=o, mark size=0.4pt, only marks] table {
        x       y      
        -40.48  -31.65 
        -40.48  -25.32 
        -40.48  -18.99 
        -40.48  -12.66 
        -40.48  -6.330 
        -40.48  0.0    
        -40.48  6.3306 
        -40.48  12.661 
        -40.48  18.991 
        -40.48  25.322 
        -40.48  31.653 
        -40.48  37.983 
        -40.48  44.314 
        -35.98  -31.65 
        -35.98  -25.32 
        -35.98  -18.99 
        -35.98  -12.66 
        -35.98  -6.330 
        -35.98  0.0    
        -35.98  6.3306 
        -35.98  12.661 
        -35.98  18.991 
        -35.98  25.322 
        -35.98  31.653 
        -35.98  44.314 
        -31.49  -31.65 
        -31.49  -25.32 
        -31.49  -18.99 
        -31.49  -12.66 
        -31.49  -6.330 
        -31.49  0.0    
        -31.49  6.3306 
        -31.49  12.661 
        -31.49  18.991 
        -31.49  25.322 
        -31.49  31.653 
        -31.49  37.983 
        -31.49  44.314 
        -26.99  -31.65 
        -26.99  -25.32 
        -26.99  -18.99 
        -26.99  -12.66 
        -26.99  -6.330 
        -26.99  0.0    
        -26.99  6.3306 
        -26.99  12.661 
        -26.99  18.991 
        -26.99  25.322 
        -26.99  31.653 
        -26.99  37.983 
        -26.99  44.314 
        -22.49  -31.65 
        -22.49  -25.32 
        -22.49  -18.99 
        -22.49  -12.66 
        -22.49  -6.330 
        -22.49  0.0    
        -22.49  6.3306 
        -22.49  12.661 
        -22.49  18.991 
        -22.49  25.322 
        -22.49  31.653 
        -22.49  37.983 
        -22.49  44.314 
        -17.99  -31.65 
        -17.99  -25.32 
        -17.99  -18.99 
        -17.99  -12.66 
        -17.99  -6.330 
        -17.99  0.0    
        -17.99  6.3306 
        -17.99  12.661 
        -17.99  25.322 
        -17.99  31.653 
        -17.99  37.983 
        -17.99  44.314 
        -13.49  -31.65 
        -13.49  -25.32 
        -13.49  -18.99 
        -13.49  -12.66 
        -13.49  -6.330 
        -13.49  0.0    
        -13.49  6.3306 
        -13.49  12.661 
        -13.49  18.991 
        -13.49  25.322 
        -13.49  31.653 
        -13.49  37.983 
        -13.49  44.314 
        -8.997  -31.65 
        -8.997  -25.32 
        -8.997  -18.99 
        -8.997  -12.66 
        -8.997  -6.330 
        -8.997  0.0    
        -8.997  6.3306 
        -8.997  12.661 
        -8.997  18.991 
        -8.997  25.322 
        -8.997  31.653 
        -8.997  37.983 
        -8.997  44.314 
        -4.498  -31.65 
        -4.498  -25.32 
        -4.498  -18.99 
        -4.498  -12.66 
        -4.498  -6.330 
        -4.498  0.0    
        -4.498  6.3306 
        -4.498  12.661 
        -4.498  18.991 
        -4.498  25.322 
        -4.498  31.653 
        -4.498  37.983 
        -4.498  44.314 
        0.0     -31.65 
        0.0     -25.32 
        0.0     -18.99 
        0.0     -12.66 
        0.0     -6.330 
        0.0     0.0    
        0.0     18.991 
        0.0     25.322 
        0.0     31.653 
        0.0     37.983 
        0.0     44.314 
        4.4986  -31.65 
        4.4986  -25.32 
        4.4986  -18.99 
        4.4986  -12.66 
        4.4986  -6.330 
        4.4986  6.3306 
        4.4986  12.661 
        4.4986  18.991 
        4.4986  25.322 
        4.4986  31.653 
        4.4986  37.983 
        4.4986  44.314 
        8.9973  -31.65 
        8.9973  -25.32 
        8.9973  -18.99 
        8.9973  -12.66 
        8.9973  6.3306 
        8.9973  12.661 
        8.9973  18.991 
        8.9973  25.322 
        8.9973  31.653 
        8.9973  37.983 
        8.9973  44.314 
        13.496  -31.65 
        13.496  -25.32 
        13.496  -18.99 
        13.496  -6.330 
        13.496  0.0    
        13.496  6.3306 
        13.496  12.661 
        13.496  18.991 
        13.496  25.322 
        13.496  31.653 
        13.496  37.983 
        13.496  44.314 
        17.994  -31.65 
        17.994  -25.32 
        17.994  -18.99 
        17.994  -6.330 
        17.994  0.0    
        17.994  6.3306 
        17.994  12.661 
        17.994  18.991 
        17.994  25.322 
        17.994  31.653 
        17.994  37.983 
        17.994  44.314 
        22.493  -31.65 
        22.493  -25.32 
        22.493  -18.99 
        22.493  -12.66 
        22.493  -6.330 
        22.493  0.0    
        22.493  6.3306 
        22.493  12.661 
        22.493  18.991 
        22.493  25.322 
        22.493  31.653 
        22.493  37.983 
        22.493  44.314 
        26.992  -31.65 
        26.992  -12.66 
        26.992  -6.330 
        26.992  0.0    
        26.992  6.3306 
        26.992  12.661 
        26.992  18.991 
        26.992  25.322 
        26.992  31.653 
        26.992  37.983 
        26.992  44.314 
        31.490  -31.65 
        31.490  -25.32 
        31.490  -18.99 
        31.490  -12.66 
        31.490  -6.330 
        31.490  0.0    
        31.490  6.3306 
        31.490  12.661 
        31.490  18.991 
        31.490  25.322 
        31.490  31.653 
        31.490  37.983 
        31.490  44.314 
      };
      \addplot[color=blue, mark=+, only marks, 
               point meta=explicit symbolic, nodes near coords,
               visualization depends on=\thisrow{angle} \as \angle,
               every node near coord/.style={font=\tiny, anchor=\angle}]
        table [meta index=2] {
        x       y       label                           angle
        8.9973  0.0     $L7a1$                          200
        0.0     6.3306  $t07828$                        270
        0.0     12.661  $10^{3}_{27}$                   270
        4.4986  0.0     $v1859(-1,3)$                   15
      };
      \addplot[color=red, mark=x, only marks, 
               point meta=explicit symbolic, nodes near coords,
               visualization depends on=\thisrow{angle} \as \angle,
               every node near coord/.style={font=\tiny, anchor=\angle}]
        table [meta index=2] {
        x       y       label                           angle
        17.994  -12.66  $s781$                          225
        26.992  -25.32  $L7a1$                          270
        -35.98  37.983  $10^{3}_{27}$                   270
        13.496  -12.66  $t08046$                        15
        26.992  -18.99  $o9_{39892}$                    270
        8.9973  -6.330  $m306$                          200
        -17.99  18.991  $t07828$                        270
      };
    \end{axis}
  \end{tikzpicture}

  ~

  \begin{tabular}{llll} \hline
    Manifold & Volume & Type & As linear combination \\ \hline
    $v1859(-1,3)$ & $4.4986\dotsc$ & geometric & $1\cdot\vol(v1859(-1,3))+0\cdot\vol(t07828)$ \\
    $t07828$ & $6.3306\dotsc$ & geometric & $0\cdot\vol(v1859(-1,3))+1\cdot\vol(t07828)$ \\
    $L7a1$ & $8.9973\dotsc$ & geometric & $2\cdot\vol(v1859(-1,3))+0\cdot\vol(t07828)$ \\
    $10^{3}_{27}$ & $12.661\dotsc$ & geometric & $0\cdot\vol(v1859(-1,3))+2\cdot\vol(t07828)$ \\
    $m306$ & $2.6667\dotsc$ & exotic & $2\cdot\vol(v1859(-1,3))-1\cdot\vol(t07828)$ \\
    $s781$ & $5.3334\dotsc$ & exotic & $4\cdot\vol(v1859(-1,3))-2\cdot\vol(t07828)$ \\
    $o9_{39892}$ & $8.0002\dotsc$ & exotic & $6\cdot\vol(v1859(-1,3))-3\cdot\vol(t07828)$ \\
    $10^{3}_{27}$ & $1.9942\dotsc$ & exotic & $-8\cdot\vol(v1859(-1,3))+6\cdot\vol(t07828)$ \\
    $L7a1$ & $1.6696\dotsc$ & exotic & $6\cdot\vol(v1859(-1,3))-4\cdot\vol(t07828)$ \\
    $t07828$ & $0.9971\dotsc$ & exotic & $-4\cdot\vol(v1859(-1,3))+3\cdot\vol(t07828)$ \\
    $t08046$ & $0.8348\dotsc$ & exotic & $3\cdot\vol(v1859(-1,3))-2\cdot\vol(t07828)$ \\
  \end{tabular}
  \caption{$p(x) = x^4-3x^2+4$, root $-1.322\dotsc+0.5i$, prospective
  basis: $\vol(v1859(-1,3))$, $\vol(t07828)$ with fit ratio 1.}
  \label{fig:v1859-lattice}
\end{figure}

Figure~\ref{fig:v1859-lattice} represents a typical ``good'' lattice
from our data. We obtained a substantial number of distinct volumes
(each volume is recorded many times in our census), and we have a number
of pairs of volumes which differ by exactly one of our conjectured
basis elements.

\begin{figure}[h]
  \begin{tikzpicture}[framed]
    \begin{axis}[
                 xlabel={Projection to generator $\vol(v3318)$},
                 ylabel={Projection to generator $\vol(L14n54610)$},
                ]
      \addplot[color=gray, mark=o, mark size=0.4pt, only marks] table {
        x       y      
        -51.60  -47.06 
        -51.60  -31.37 
        -51.60  -15.68 
        -51.60  0.0    
        -51.60  15.688 
        -51.60  31.376 
        -51.60  47.064 
        -51.60  62.752 
        -45.15  -47.06 
        -45.15  -31.37 
        -45.15  -15.68 
        -45.15  0.0    
        -45.15  15.688 
        -45.15  31.376 
        -45.15  62.752 
        -38.70  -47.06 
        -38.70  -31.37 
        -38.70  -15.68 
        -38.70  0.0    
        -38.70  15.688 
        -38.70  31.376 
        -38.70  47.064 
        -38.70  62.752 
        -32.25  -47.06 
        -32.25  -31.37 
        -32.25  -15.68 
        -32.25  0.0    
        -32.25  15.688 
        -32.25  31.376 
        -32.25  47.064 
        -32.25  62.752 
        -25.80  -47.06 
        -25.80  -31.37 
        -25.80  -15.68 
        -25.80  0.0    
        -25.80  15.688 
        -25.80  47.064 
        -25.80  62.752 
        -19.35  -47.06 
        -19.35  -31.37 
        -19.35  -15.68 
        -19.35  0.0    
        -19.35  15.688 
        -19.35  31.376 
        -19.35  47.064 
        -19.35  62.752 
        -12.90  -47.06 
        -12.90  -31.37 
        -12.90  -15.68 
        -12.90  0.0    
        -12.90  31.376 
        -12.90  47.064 
        -12.90  62.752 
        -6.450  -47.06 
        -6.450  -31.37 
        -6.450  -15.68 
        -6.450  0.0    
        -6.450  31.376 
        -6.450  47.064 
        -6.450  62.752 
        0.0     -47.06 
        0.0     -31.37 
        0.0     -15.68 
        0.0     0.0    
        0.0     15.688 
        0.0     31.376 
        0.0     47.064 
        0.0     62.752 
        6.4506  -47.06 
        6.4506  -31.37 
        6.4506  -15.68 
        6.4506  15.688 
        6.4506  31.376 
        6.4506  47.064 
        6.4506  62.752 
        12.901  -47.06 
        12.901  -31.37 
        12.901  -15.68 
        12.901  0.0    
        12.901  15.688 
        12.901  31.376 
        12.901  47.064 
        12.901  62.752 
        19.352  -47.06 
        19.352  -31.37 
        19.352  0.0    
        19.352  15.688 
        19.352  31.376 
        19.352  47.064 
        19.352  62.752 
        25.802  -47.06 
        25.802  -31.37 
        25.802  -15.68 
        25.802  0.0    
        25.802  15.688 
        25.802  31.376 
        25.802  47.064 
        25.802  62.752 
        32.253  -47.06 
        32.253  -15.68 
        32.253  0.0    
        32.253  15.688 
        32.253  31.376 
        32.253  47.064 
        32.253  62.752 
        38.704  -47.06 
        38.704  -31.37 
        38.704  -15.68 
        38.704  0.0    
        38.704  15.688 
        38.704  31.376 
        38.704  47.064 
        38.704  62.752 
      };
      \addplot[color=blue, mark=+, only marks, 
               point meta=explicit symbolic, nodes near coords,
               visualization depends on=\thisrow{angle} \as \angle,
               every node near coord/.style={font=\tiny, anchor=\angle}]
        table [meta index=2] {
        x       y       label                           angle
        6.4506  0.0     $v3318$                         270
        0.0     15.69   $L14n534610$                    165
      };
      \addplot[color=red, mark=x, only marks, 
               point meta=explicit symbolic, nodes near coords,
               visualization depends on=\thisrow{angle} \as \angle,
               every node near coord/.style={font=\tiny, anchor=\angle}]
        table [meta index=2] {
        x       y       label                           angle
        19.352  -15.68  $K12n809$                       15
        25.802  -23.53  $t09825$                        15
        -6.450  15.688  $L13n5993$                      270
        -25.80  31.376  $10^{3}_{5}$                    270
        32.253  -31.37  $v3318$                         15
        12.901  -7.844  $t09825$                        195
        -12.90  15.688  $v3548$                         15
        -45.15  47.064  $L13n5993$                      270
        9.6760  -7.844  $v2489$                         15
      };
    \end{axis}
  \end{tikzpicture}

  ~

  \begin{tabular}{llll} \hline
    Manifold & Volume & Type & As linear combination \\ \hline
    $v3318$ & $6.4506\dotsc$ & geometric & $1\cdot\vol(v3318)+0\cdot\vol(L14n54610)$ \\
    $L14n534610$ & $15.6881\dotsc$ & geometric & $0\cdot\vol(v3318)+1\cdot\vol(L14n54610)$ \\
    $t09825$ & $2.2704\dotsc$ & exotic & $4\cdot\vol(v3318)-1.5\cdot\vol(L14n54610)$ \\
    $v3318$ & $0.8770\dotsc$ & exotic & $5\cdot\vol(v3318)-2\cdot\vol(L14n54610)$ \\
    $10^{3}_{5}$ & $5.5736\dotsc$ & exotic & $-4\cdot\vol(v3318)+2\cdot\vol(L14n54610)$ \\
    $L13n5993$ & $1.9097\dotsc$ & exotic & $-7\cdot\vol(v3318)+3\cdot\vol(L14n54610)$ \\
    $K12n809$ & $3.6638\dotsc$ & exotic & $3\cdot\vol(v3318)-1\cdot\vol(L14n54610)$ \\
    $L13n5993$ & $9.2374\dotsc$ & exotic & $-1\cdot\vol(v3318)+1\cdot\vol(L14n54610)$ \\
    $v2489$ & $1.8319\dotsc$ & exotic & $1.5\cdot\vol(v3318)-0.5\cdot\vol(L14n54610)$ \\
    $t09825$ & $5.0572\dotsc$ & exotic & $2\cdot\vol(v3318)-0.5\cdot\vol(L14n54610)$ \\
    $v3548$ & $2.7868\dotsc$ & exotic & $-2\cdot\vol(v3318)+1\cdot\vol(L14n54610)$ \\
  \end{tabular}
  \caption{$p(x) = x^4+x^2-2x+1$, root $-0.624\dotsc+1.300\dotsc i$,
  prospective basis: $\vol(v3318)$, $\vol(L14n54610)$ with fit ratio 2.}
  \label{fig:v3318-lattice}
\end{figure}

Figure~\ref{fig:v3318-lattice} represents a typical ``almost good''
lattice from our data.  Our fit ratio is 2, which points out that we
are unable to fit the exotic volumes of $v2489$ and $t09825$ (either
of them) completely into our lattice. Nonetheless, this lattice allows
us to conjecture the existence of smaller manifolds which would
``fix'' this lattice. For example, we might suppose that the nearby
exotic volumes of $v2489$ and $t09825$ differ by a generator (or,
perhaps, a multiple of a generator): this would imply the existence of
a manifold with volume $\frac{\vol(v3318)}{2} \approx 3.2253$ (this is
by no means the only volume which would ``fix'' the lattice).

\clearpage

\printbibliography
