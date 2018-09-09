use Finance::QuoteHist;
  $q = Finance::QuoteHist->new
     (
      symbols    => [qw(IBM UPS AMZN)],
      start_date => '04/01/2018', # or '1 year ago', see Date::Manip
      end_date   => '04/06/2018',
     );

  # Quotes
  foreach $row ($q->quotes()) {
    ($symbol, $date, $open, $high, $low, $close, $volume) = @$row;
    print $symbol, $date, $open, $high, $low, $close, $volume;
  }

  # Splits
  foreach $row ($q->splits()) {
     ($symbol, $date, $post, $pre) = @$row;
  }

  # Dividends
  foreach $row ($q->dividends()) {
     ($symbol, $date, $dividend) = @$row;
  }

  # Culprit
  $fetch_class = $q->quote_source('IBM');

