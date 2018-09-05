list1 = ['&gt;', '&lowast;', '&Omega;', '&rho;', '&mu;', '&acute;', '&ograve;', '&amp;', '&ordm;', '&alpha;', '&ang;', '&uarr;', '&theta;', '&beta;', '&prime;', '&omega;', '&rdquo;', '&times;', '&nabla;', '&omicron;', '&le;', '&not;', '&lambda;', '&cap;', '&tau;', '&deg;', '&nbsp;', '&quot;', '&oacute;', '&rarr;', '&sect;', '&macr;', '&piv;', '&darr;', '&ldquo;', '&zwnj;', '&chi;', '&xi;', '&kappa;', '&gamma;', '&forall;', '&radic;', '&hellip;', '&frasl;', '&epsilon;', '&zwj;', '&rsquo;', '&bull;', '&larr;', '&hearts;', '&or;', '&sigma;', '&mdash;', '&iota;', '&lsquo;', '&lt;', '&yen;', '&ndash;', '&oline;', '&pi;']
list2 = ['&#186;', '&#175;', '&#160;', '&#128557;', '&#128024;', '&#249;', '&lt;', '&#39;', '&gt;', '&#243;', '&#215;', '&amp;', '&#172;', '&quot;', '&#30528;', '&#173;', '&#165;', '&#233;', '&#225;', '&#180;', '&#183;', '&#128051;', '&#176;', '&#128522;']
list3 = list1 + list2
print(set(list3), '\n', len(set(list3)))

