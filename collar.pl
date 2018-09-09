# !/usr/bin/perl -w

use strict;

# import module
use lib '../lib';
use Finance::Quote;

use Data::Dumper;

# create object
my $q = Finance::Quote->new();

my %quotes = $q->fetch("NYSE","IBM");
print "NYSE by YAHOO", $quotes{"IBM","name"}, "\n";
print "Last Price", $quotes{"IBM","last"}, "\n";
exit;

### RSPmy %data = $q->fetch('nyse', 'APPL');
### RSPprint Data::Dumper->Dump([\%data]);
### RSPexit;
### RSP
### RSP# print "The current price of Apple on the NYSE is ".$data{'AAPL','price'};
### RSP
### RSPmy @sources = $q->sources();
### RSPprint "Available sources are: ";
### RSP
### RSPforeach my $s(@sources) {
### RSP	print "$s ",;
### RSP}
### RSP
### RSPexit;
### RSP
### RSPprint "Stock Name: ";
### RSPmy $stockname = <STDIN>;
### RSPchomp ($stockname);
### RSP
### RSPmy $price_per_share = 0.0;
### RSPprint "Underlaying Price: ";
### RSP$price_share = <STDIN>;
### RSPchomp($price_share);
### RSP
### RSPprint "Expiration Date: ";
### RSPmy $option_exp = <STDIN>;
### RSPchomp ($option_exp);
### RSP
### RSPprint "STRIKE Price: ";
### RSPmy $strikeprice = <STDIN>;
### RSPchomp($stockprice);
### RSP
### RSPprint "Premium Price: ";
### RSPmy $option_premium = <STDIN>;
### RSPchomp ($option_premium);
### RSP
### RSPmy $sharesPerContract = 100;
### RSP
### RSPmy $total_underlaying = $sharesPerContract * $price_share; 
### RSPmy $total_premium = $option_premium * $sharesPerContract;
### RSP
### RSPprint "Strike Increase: ";
### RSPmy $increasestrike = <STDIN>;
### RSPchomp ($increasestrike);
### RSP
### RSPprintf "Underlaying Stock: %10s\t", $stockname;
### RSPprintf "Initial Price: %6.2f\t", $price_share;
### RSPprintf "Total Price: %6.2f\t", $total_underlaying;
### RSPprintf "Premium Per Contract: %4.2f\t", $option_premium;
### RSPprintf "Total Price Contract: %6.2f\t", $total_premium;
### RSPmy $break_even_point = $price_share - $option_premium;
### RSPprintf "Break Even Point:: %6.2f\t", $break_even_point;
### RSPprintf "\n";
### RSP
### RSPexit;
### RSP
### RSPmy $intrinsic = 0.0;
### RSPmy$strikecount = 0;
### RSPmy $intrinsic = 0;
### RSPprintf "Current Price: %6.2f\n", $stockprice;
### RSPforeach $strikecount (0..9) {
### RSP	# $intrinsic = $strikeprice - $stockprice;
### RSP	$intrinsic = $stockprice - $strikeprice;
### RSP	# print "Strike Price: ", $strikeprice, "\tIntrinsic Value = ", $intrinsic, "\n";
### RSP	printf "Strike Price: %6.2f\t", $strikeprice;
### RSP	printf "Intrinsic Value = %6.2f\n", $intrinsic;
### RSP	$strikeprice = $strikeprice - $increasestrike;
### RSP}
