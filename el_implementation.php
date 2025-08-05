<?php
function turnleft($direction) {
	$left=array();
	$left[0][1]=[-1,0];
	$left[-1][0]=[0,-1];
	$left[0][-1]=[1,0];
	$left[1][0]=[0,1];
	if (!isset($left[$direction[0]][$direction[1]])) {
		die("Not a valid direction.");
	}
	return $left[$direction[0][$direction[1]]];
}
function turnright($direction) {
	$right=array();
	$right[-1][0]=[0,1];
	$right[0][-1]=[-1,0];
	$right[1][0]=[0,-1];
	$right[0][1]=[1,0];
	if (!isset($right[$direction[0]][$direction[1]])) {
		die("Not a valid direction.");
	}
	return $right[$direction[0][$direction[1]]];
}
function move($coord,$direction) {
	$coord[0]+=$direction[0];
	$coord[1]+=$direction[1];
	return $coord;
}
function add($coord,$system,$value) {
	$system[$coord[0]][$coord[1]]=$value;
	return $system;
}
function moveant($system,$direction,$position,$command) {
	$totest=$system[$position[0]][$position[1]];
	if ($totest==0) {
		$system[$position[0]][$position[1]]=1;
	} else {
		$system[$position[0]][$position[1]]=0;
	}
	if ($command=="c") {
		if ($totest==0) {
			$command="r";
		} else {
			$command="l";
		}
	}
	if ($command=="l") {
		$direction=turnleft($direction);
	}
	if ($command=="r") {
		$direction=turnright("$direction");
	}
	$position=move($position,$direction);
	$system=add($position,$system,0);
	return [$system,$direction,$position];
}
function langton($commands,$system=array(0=>array(0=>0)),$direction=[1,0],$position=[0,0]) {
	$commands=str_split($commands);
	foreach ($commands as $i) {
		$result=moveant($system,$direction,$position,$i);
		$system=$result[0];
		$direction=$result[1];
		$position=$result[2];
	}
	return [$system,$direction,$position];
}
//print_r(langton("l"));
?>
