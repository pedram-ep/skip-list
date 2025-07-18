package main

import (
	"fmt"
	"math/rand"
	// "time"
)


const (
	maxHeight    = 32
	probability = 0.5
)

type Node struct {
	key int
	value interface{}
	forward []*Node
}

type SkipList struct {
	height int
	length int
	head *Node
}

func NewSkipList() *SkipList {
	head := &Node{
		forward: make([]*Node, maxHeight),
	}
	return &SkipList{
		height: 1,
		head: head,
		length: 0,
	}
}

func (sl *SkipList) randomHeight() int {
	height := 1
	for rand.Float64() < probability && height < maxHeight {
		height++
	}
	return height
}

func (sl *SkipList) insert(key int, value interface{}) {
	update := make([]*Node, maxHeight)
	current := sl.head

	for i := sl.height - 1; i>= 0; i-- {
		for current.forward[i] != nil && current.forward[i].key < key {
			current = current.forward[i]
		}
		update[i] = current
	}

	current = current.forward[0]

	if current != nil && current.key == key {
		current.value = value
		return
	}

	newHeight := sl.randomHeight()

	if newHeight > sl.height {
		for i := sl.height; i < newHeight; i++ {
			update[i] = sl.head
		}
		sl.height = newHeight
	}

	newNode := &Node{
		key: key,
		value: value,
		forward: make([]*Node, newHeight),
	}

	for i := 0; i < newHeight; i++ {
		newNode.forward[i] = update[i].forward[i]
		update[i].forward[i] = newNode
	}

	sl.length++
}

func (sl *SkipList) search(key int) (interface{}, bool) {
	current := sl.head
	for i := sl.height - 1; i >= 0; i-- {
		for current.forward[i] != nil && current.forward[i].key < key {
			current = current.forward[i]
		}
	}

	current = current.forward[0]

	if current != nil && current.key == key {
		return current.value, true
	}
	return nil, false
}

func (sl *SkipList) delete(key int) {
	update := make([]*Node, maxHeight)
	current := sl.head

	for i := sl.height - 1; i >= 0; i-- {
		for current.forward[i] != nil && current.forward[i].key < key {
			current = current.forward[i]
		}
		update[i] = current
	}

	current = current.forward[0]
	if current == nil || current.key != key {
		return
	}

	for i := 0; i < sl.height; i++ {
		if update[i].forward[i] != current {
			break
		}
		update[i].forward[i] = current.forward[i]
	}
	
	for sl.height > 1 && sl.head.forward[sl.height-1] == nil {
		sl.height--
	}

	sl.length--
}

func main() {
	// rand.Seed(time.Now().UnixNano())
	sl := NewSkipList()

	sl.insert(3, "data3")
	sl.insert(6, "data6")
	sl.insert(7, "data7")
	sl.insert(9, "data9")
	sl.insert(12, "data12")

	if value, found := sl.search(6); found {
		fmt.Println("Found key 6:", value)
	}

	sl.delete(6)
	if _, found := sl.search(6); !found {
		fmt.Println("Key 6 deleted")
	}
}