---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut Hamoon Mousavi"
section_id: sec-029-73-macro-macro-name-template
section_title: "macro: macro <name> <template>"
section_number: 7.3
pages: 27-29
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
doc_brief: "Automatic Theorem Proving in Walnut Hamoon Mousavi — 34 sections: Introduction; Basics; Words and Automata"
---
Recall that a subword W [i..i +n −1] is a palindrome if W [i +k] = W [i +n −1−k] for all k < n. The following calculates the
palindromes in the Thue-Morse word11:
11In speciﬁc terms, this calculation constructs an automaton accepting (i,n)’s for which W [i..i +n −1] is a palindrome.
27
eval thue_pal "Ak k<n => T[ i+k] = T[ i+n−1−k] " ;
Now in order to calculate palindromes for the Fibonacci word, one has to type the entire predicate above, letter for letter,
except for the substitution of T by F:
eval fibonacci_pal " ?msd_fib Ak k<n => F[ i+k] = F[ i+n−1−k] " ;
There are many other example where one would like to calculate the same calculation for many different words. Similar
to the def command, the macro command is a mechanism for avoiding dull repetitions. For the palindrome example, one
could deﬁne the following macro:
macro pal "?%0 Ak k<n => %1[i+k] = %1[i+n−1−k] " ;
This command saves the template ?\%0 Ak k<n => \%1[i+k] = \%1[i+n−1−k] in a ﬁle named pal.txt in the directory “/Wal-
nut/Macro Library/”. Then to calculate palindromes for the Thue-Morse word, using a similar syntax to function calls, one
could write:
eval thue_pal "#pal (msd_2,T) " ;
The ﬁrst step in computing eval and def commands is a preprocessing task in which all macros will be replaced by their
template strings. In our example, Walnut replaces the #pal(msd_2,T) by the template, saved in the ﬁle pal.txt, then substitutes
%0 and %1 by msd_2 and T, respectively. Now see how easily one can calculate plaindromes for the Fibonacci word:
eval fibonacci_pal "#pal ( msd_fib , F) " ;
The important difference between the macro and the def commands is that the macro takes a template and stores it
unaltered as a string, whereas the def command takes a predicate and stores the automaton calculated for that predicate. The
macro saves the user from typing the same template over and over, while the def command saves the user from calculating
the same predicate over and over.
Let us see a second example. An important automaton for any word is one that accepts triples (i, j,n) for which subwords
of length n starting at positions i and j are the same. This automaton, which we call factoreq, shows up in many different
calculations, a notable one being border calculation. Recall that W [i..i + n −1] has a border of length m if subwords
W [i..i +m −1] and W [i +n −m..i +n −1] are equal. In other words, the W [i..i +n −1] has a border of length m if factoreq
accepts (i,i +n −m,m). In Walnut, for Thue-Morse, this is the same as writing:
def thue_factoreq "Ak k<n => T[ i+k]=T[ j+k] " ;
eval thue_border "$1 <= m & m <= n & $thue_factoreq ( i , i+n−m,m) " ;
Now to calculate for Fibonacci, this becomes:
def fibonacci_factoreq " ?msd_fib Ak k<n => F[ i+k]=F[ j+k] " ;
eval fibonacci_border " ?msd_fib 1 <= m & m <= n & $fibonacci_factoreq ( i , i+n−m,m) " ;
Using macros, one could capture the essence of the above calculations as follows:
macro factoreq "?%0 Ak k<n => %1[i+k]=%1[ j+k] " ;
macro border "?%0 1 <= m & m <= n & #%1_factoreq ( i , i+n−m,m) " ;
With these macros at hand, one can calculate factoreq and border for many different words. For example, for Thue-Morse
the calculation becomes:
def thue_factoreq "#factoreq (msd_2,T) " ;
eval thue_border "#border (msd_2, thue ) " ;
and for the Fibonacci it becomes:
def fibonacci_factoreq "#factoreq ( msd_fib , F) " ;
eval fibonacci_border "#border ( msd_fib , fibonacci ) " ;
Walnut does not accept nested macro/function calls, i.e., none of the followings are accepted: $f (..., $g (...),...) ,
$f (...,# m (...),...) , #m(...,#n (...),...) , #m(...,$g (...),...) .
28
7.4
