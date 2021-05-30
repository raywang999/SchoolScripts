for i in {1998..2021}
do
	curl https://cemc.uwaterloo.ca/contests/past_contests/$i/$i\EuclidContest.pdf > c$i.pdf
	curl https://cemc.uwaterloo.ca/contests/past_contests/$i/$i\EuclidSolution.pdf > s$i.pdf
done

exit 0
