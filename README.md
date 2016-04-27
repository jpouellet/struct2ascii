# struct2ascii

Turns simple struct contents into "RFC artwork"-style ASCII diagrams.

Very WIP and could definitely be cleaner, but sufficient for my initial use.
I might clean it up one day. I think it'd be nice to have similar functionality
as part of [xml2rfc](http://xml2rfc.ietf.org/) in an `<artwork type="struct">`
or something.

## Example

Turns this:
```
	uint16_t some;
	uint8_t little;
	uint8_t fields;
	uint8_t and;
	uint8_t an_array[3];
	uint32_t bigger;
	uint64_t even_bigger;
	uint32_t huge[256];
```

into this:
```
                        1                   2                   3   
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |              some             |     little    |     fields    |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |      and      |                    an_array                   |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                             bigger                            |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                          even_bigger                          |
   |                                                               |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                                                               |
   ~                              huge                             ~
   |                                                               |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

## TODO

- arguments to set those few options hard-coded at the top
- support bit field members
- support nested structs
- support extraction directly from source via a libclang-based tool or something
  (right now things need to be non-trivially preprocessed (more than just cc -E))

Pull requests welcome :)

## License

Public domain / CC0 / wtfpl. I really don't care :)
