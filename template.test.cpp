vc<int> ans;
rev_rep(i, 10) {
    ans.eb(i);
}
assert((ans == vc<int>{9, 8, 7, 6, 5, 4, 3, 2, 1, 0}));
out(ans);
ans.clear();
rev_rep(i, 10, 5) {
    ans.eb(i);
}
out(ans);
ans.clear();
rev_rep1(i, 10) {
    ans.eb(i);
}
out(ans);
ans.clear();
rev_rep1(i, 10, 5) {
    ans.eb(i);
}
out(ans);