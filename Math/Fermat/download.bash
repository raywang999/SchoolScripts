for i in {1997..2019}
do
	curl https://www.cemc.uwaterloo.ca/contests/past_contests/$i/$i\FermatContest.pdf > c$i.pdf
	curl https://www.cemc.uwaterloo.ca/contests/past_contests/$i/$i\FermatSolution.pdf > s$i.pdf
done

exit 0
