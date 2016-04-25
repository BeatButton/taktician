package main

import (
	"bufio"
	"flag"
	"log"
	"os"
	"strconv"
	"strings"

	"nelhage.com/tak/ai"
	"nelhage.com/tak/cli"
	"nelhage.com/tak/tak"
)

var (
	white = flag.String("white", "human", "white player")
	black = flag.String("black", "human", "white player")
	size  = flag.Int("size", 5, "game size")
)

func parsePlayer(in *bufio.Reader, s string) cli.Player {
	if s == "human" {
		return cli.NewCLIPlayer(os.Stdout, in)
	}
	if s == "rand" {
		return ai.NewRandom(0)
	}
	if strings.HasPrefix(s, "rand") {
		var seed int64
		if len(s) > len("rand") {
			i, err := strconv.Atoi(s[len("rand:"):])
			if err != nil {
				log.Fatal(err)
			}
			seed = int64(i)
		}
		return ai.NewRandom(seed)
	}
	if strings.HasPrefix(s, "minimax") {
		var depth = 3
		if len(s) > len("minimax") {
			i, err := strconv.Atoi(s[len("minimax:"):])
			if err != nil {
				log.Fatal(err)
			}
			depth = i
		}
		return ai.NewMinimax(depth)
	}
	log.Fatalf("unparseable player: %s", s)
	return nil
}

func main() {
	flag.Parse()
	in := bufio.NewReader(os.Stdin)
	st := &cli.CLI{
		Config: tak.Config{Size: *size},
		Out:    os.Stdout,
		White:  parsePlayer(in, *white),
		Black:  parsePlayer(in, *black),
	}
	st.Play()
}
