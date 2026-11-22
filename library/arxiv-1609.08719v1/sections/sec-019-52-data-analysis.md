---
doc_id: arxiv-1609.08719v1
doc_title: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE"
section_id: sec-019-52-data-analysis
section_title: "Data analysis"
section_number: 5.2
pages: 12-14
source_pdf: 1609.08719v1.pdf
source_sha256: f61ff2111e9a97f9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.973
doc_brief: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE — We use a large census of hyperbolic 3-manifolds to experimentally investigate a conjecture of Neumann regarding the Bloch Group."
---
By comparing the fields we observed (under some reasonable restrictions) to a
proven-complete census under the same restrictions, we obtain an estimate
of the probability that an arbitrary field (within these restrictions)
appears in our census. If conjecture~\ref{conj:neumann-weaker} holds,
then our census samples from all possible fields. If our sample was
uniformly random, we would then expect that our census contains the same
percentage of fields with $r_2 = 1$ as for $r_2 \ne 1$.

For our calculations, we used a online census \parencite{jones2014}
of abstract number fields expressed as polynomials. For
the field restrictions we used, this census has been proven
complete. In figures~\ref{fig:observed-concrete-fields} and
\ref{fig:observed-abstract-fields}, $n$ refers to the degree of
the polynomial $p$ to which the field is associated, and $D$ is the
discriminant of the polynomial. We only consider restrictions for which
multiple values of $r_2$ are possible, and we ignore $r_2 = 4$ due to
relative scarcity of data (the total fields for $r_2 = 4$ are so numerous
that our results are scarce enough to be statistical noise).

\begin{figure}[h]
  \centering
  {\small
  \begin{tabular}{|ll|lll|lll|lll|} \hline
    \multicolumn{2}{|l|}{Restrictions} & \multicolumn{3}{c|}{$r_2 = 1$} & \multicolumn{3}{c|}{$r_2 = 2$} & \multicolumn{3}{c|}{$r_2 = 3$} \\
    $n$ & $|D|^{1/n}$ & {\small Found} & {\small Total} & \% & {\small Found} & {\small Total} & \% & {\small Found} & {\small Total} & \% \\ \hline

    $4$ & $\le 8$ & $56$ & $137$ & $40.8\%$ & $76$ & $408$ & $18.6\%$ & & & \\
    $4$ & $\le 10$ & $65$ & $444$ & $14.6\%$ & $82$ & $1100$ & $7.4\%$ & & & \\
    $4$ & $\le 12$ & $66$ & $1056$ & $6.2\%$ & $84$ & $2550$ & $3.2\%$ & & & \\
    $4$ & $\le 15$ & $66$ & $3069$ & $2.1\%$ & $84$ & $6728$ & $1.2\%$ & & & \\

    $5$ & $\le 8$ & $47$ & $77$ & $61.0\%$ & $226$ & $736$ & $30.7\%$ & & & \\
    $5$ & $\le 10$ & $65$ & $472$ & $13.7\%$ & $326$ & $3470$ & $9.3\%$ & & & \\
    $5$ & $\le 12$ & $73$ & $1670$ & $4.3\%$ & $356$ & $10992$ & $3.2\%$ & & & \\
    $5$ & $\le 15$ & $76$ & $7556$ & $1.0\%$ & $362$ & $41776$ & $.8\%$ & & & \\

    $6$ & $\le 8$ & $11$ & $40$ & $27.5\%$ & $180$ & $1222$ & $14.7\%$ & $166$ & $1851$ & $8.9\%$ \\
    $6$ & $\le 10$ & $28$ & $405$ & $6.9\%$ & $374$ & $8434$ & $4.4\%$ & $291$ & $10887$ & $2.6\%$ \\
    $6$ & $\le 12$ & $37$ & $2335$ & $1.5\%$ & $514$ & $38722$ & $1.3\%$ & $352$ & $42123$ & $.8\%$ \\
    $6$ & $\le 15$ & $48$ & $15556$ & $.3\%$ & $578$ & $204108$ & $.2\%$ & $380$ & $190995$ & $.1\%$ \\

    $7$ & $\le 10$ & $10$ & $137$ & $7.2\%$ & $276$ & $8070$ & $3.4\%$ & $391$ & $38103$ & $1.0\%$ \\
    $7$ & $\le 12$ & $14$ & $1473$ & $.9\%$ & $455$ & $57292$ & $.7\%$ & $637$ & $219879$ & $.2\%$ \\
    $7$ & $\le 15$ & $30$ & $16759$ & $.1\%$ & $599$ & $506188$ & $.1\%$ & $890$ & $1612152$ & $.0\%$ \\

    $8$ & $\le 10$ & $1$ & $22$ & $4.5\%$ & $75$ & $752$ & $9.9\%$ & $288$ & $3141$ & $9.1\%$ \\
    $8$ & $\le 12$ & $7$ & $246$ & $2.8\%$ & $199$ & $5808$ & $3.4\%$ & $584$ & $16764$ & $3.4\%$ \\
    $8$ & $\le 15$ & $11$ & $2560$ & $.4\%$ & $383$ & $50268$ & $.7\%$ & $976$ & $120111$ & $.8\%$ \\

    \hline
  \end{tabular}
  }
  \caption{Observed concrete field percentages by restriction}
  \label{fig:observed-concrete-fields}
\end{figure}

\begin{figure}[h]
  \centering
  {\small
  \begin{tabular}{|ll|lll|lll|lll|} \hline
    \multicolumn{2}{|l|}{Restrictions} & \multicolumn{3}{c|}{$r_2 = 1$} & \multicolumn{3}{c|}{$r_2 = 2$} & \multicolumn{3}{c|}{$r_2 = 3$} \\
    $n$ & $|D|^{1/n}$ & {\small Found} & {\small Total}& \% & {\small Found} & {\small Total}& \% & {\small Found} & {\small Total}& \% \\ \hline

    $4$ & $\le 8$ & $56$ & $137$ & $40.8\%$ & $60$ & $204$ & $29.4\%$ & & & \\
    $4$ & $\le 10$ & $65$ & $444$ & $14.6\%$ & $66$ & $550$ & $12.0\%$ & & & \\
    $4$ & $\le 12$ & $66$ & $1056$ & $6.2\%$ & $68$ & $1275$ & $5.3\%$ & & & \\
    $4$ & $\le 15$ & $66$ & $3069$ & $2.1\%$ & $68$ & $3364$ & $2.0\%$ & & & \\

    $5$ & $\le 8$ & $47$ & $77$ & $61.0\%$ & $168$ & $368$ & $45.6\%$ & & & \\
    $5$ & $\le 10$ & $65$ & $472$ & $13.7\%$ & $264$ & $1735$ & $15.2\%$ & & & \\
    $5$ & $\le 12$ & $73$ & $1670$ & $4.3\%$ & $294$ & $5496$ & $5.3\%$ & & & \\
    $5$ & $\le 15$ & $76$ & $7556$ & $1.0\%$ & $300$ & $20888$ & $1.4\%$ & & & \\

    $6$ & $\le 8$ & $11$ & $40$ & $27.5\%$ & $162$ & $611$ & $26.5\%$ & $143$ & $617$ & $23.1\%$ \\
    $6$ & $\le 10$ & $28$ & $405$ & $6.9\%$ & $350$ & $4217$ & $8.2\%$ & $263$ & $3629$ & $7.2\%$ \\
    $6$ & $\le 12$ & $37$ & $2335$ & $1.5\%$ & $489$ & $19361$ & $2.5\%$ & $324$ & $14041$ & $2.3\%$ \\
    $6$ & $\le 15$ & $48$ & $15556$ & $.3\%$ & $553$ & $102054$ & $.5\%$ & $352$ & $63665$ & $.5\%$ \\

    $7$ & $\le 10$ & $10$ & $137$ & $7.2\%$ & $271$ & $4035$ & $6.7\%$ & $383$ & $12701$ & $3.0\%$ \\
    $7$ & $\le 12$ & $14$ & $1473$ & $.9\%$ & $450$ & $28646$ & $1.5\%$ & $629$ & $73293$ & $.8\%$ \\
    $7$ & $\le 15$ & $30$ & $16759$ & $.1\%$ & $594$ & $253094$ & $.2\%$ & $882$ & $537384$ & $.1\%$ \\

    $8$ & $\le 10$ & $1$ & $22$ & $4.5\%$ & $75$ & $376$ & $19.9\%$ & $286$ & $1047$ & $27.3\%$ \\
    $8$ & $\le 12$ & $7$ & $246$ & $2.8\%$ & $199$ & $2904$ & $6.8\%$ & $582$ & $5588$ & $10.4\%$ \\
    $8$ & $\le 15$ & $11$ & $2560$ & $.4\%$ & $383$ & $25134$ & $1.5\%$ & $974$ & $40037$ & $2.4\%$ \\

    \hline
  \end{tabular}
  }
  \caption{Observed abstract field percentages by restriction}
  \label{fig:observed-abstract-fields}
\end{figure}

Figure~\ref{fig:observed-concrete-fields} implies, in general, a
negative correlation between the number of complex places of the
field and the probability that it is exhibited by some manifold.
Figure~\ref{fig:observed-abstract-fields} offers hope for an explanation.

While figure~\ref{fig:observed-concrete-fields}
lists the observed percentage of concrete number fields,
figure~\ref{fig:observed-abstract-fields} lists the observed percentage
of fields considered as $\mathbb{Q}[x]/\langle p \rangle$: in particular,
we treat any two concrete fields arising from different roots of the
same polynomial as identical. The percentages are relatively even
across rows in this case, which supports that our census was selecting
from all possible abstract number fields. This partially supports
conjecture~\ref{conj:neumann-weaker}, and more solidly supports the
following weaker version.

\begin{conjecture}
  \label{conj:only-abstract-represented}
  Every non-real abstract number field $\mathbb{Q}[x]/\langle p \rangle$
  arises as abstract number field associated to the invariant trace
  field of some hyperbolic manifold.
\end{conjecture}
