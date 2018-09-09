#!/usr/bin/perl
print "Stock Price: ";
my $stockprice = <STDIN>;
chomp($stockprice);
print "Strike Price: ";
my $strikeprice = <STDIN>;
chomp ($strikeprice);
print "Strike Increase: ";
my $increasestrike = <STDIN>;
chomp ($increasestrike);
my $intrinsic = 0.0;
my$strikecount = 0;
my $intrinsic = 0;
printf "Current Price: %6.2f\n", $stockprice;
foreach $strikecount (0..9) {
	# $intrinsic = $strikeprice - $stockprice;
	$intrinsic = $stockprice - $strikeprice;
	# print "Strike Price: ", $strikeprice, "\tIntrinsic Value = ", $intrinsic, "\n";
	printf "Strike Price: %6.2f\t", $strikeprice;
	printf "Intrinsic Value = %6.2f\n", $intrinsic;
	$strikeprice = $strikeprice - $increasestrike;
}
