product_data = {
    "A": {
        "price": 50,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 5,
                "value": 200,
                "has_action": False
            },
            "offer_2": {
                "quantity": 3,
                "value": 130,
                "has_action": False
            }    
        }
    },
    "B": {
        "price": 30,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 2,
                "value": 45,
                "has_action": False
            }    
        }
    },
    "C": {
        "price": 20,
        "has_offer": False,
        "offers":{}
    },
    "D": {
        "price": 15,
        "has_offer": False,
        "offers": {}
    },
    "E": {
        "price": 40,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 1,     #quantity of 1 doesn't break the maths by not dividing by 0
                "value": 0,        #value of 0 allows for skipping of offer price reduction
                "has_action": True,
                "action": {
                    "quantity": 2,
                    "action_type": "free_item",     # one free B item won't change the value of the total
                    "sku_affected": "B",            # so this offer won't affect anything and is not needed in calculation
                    "number": 1                     # turns out this is not the case :(
                }
            }
        }
    },  
    "F": {
        "price": 10,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 1,     
                "value": 0,        
                "has_action": True,
                "action": {
                    "quantity": 3,
                    "action_type": "free_item",     
                    "sku_affected": "F",            
                    "number": 1                     
                }
            }
        }
    },
    "G": {
        "price": 20,
        "has_offer": False,
        "offers":{}
    },
    "H": {
        "price": 10,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 10,
                "value": 80,
                "has_action": False
            },
            "offer_2": {
                "quantity": 5,
                "value": 45,
                "has_action": False
            }    
        }
    },
    "I": {
        "price": 35,
        "has_offer": False,
        "offers":{}
    },
    "J": {
        "price": 60,
        "has_offer": False,
        "offers":{}
    }, 
    "K": {
        "price": 80,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 2,
                "value": 150,
                "has_action": False
            }    
        }
    },
    "L": {
        "price": 90,
        "has_offer": False,
        "offers":{}
    },
    "M": {
        "price": 15,
        "has_offer": False,
        "offers":{}
    },
    "N": {
        "price": 40,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 1,     
                "value": 0,        
                "has_action": True,
                "action": {
                    "quantity": 3,
                    "action_type": "free_item",     
                    "sku_affected": "M",            
                    "number": 1                     
                }
            }
        }
    },
    "O": {
        "price": 10,
        "has_offer": False,
        "offers":{}
    },
    "P": {
        "price": 50,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 5,
                "value": 200,
                "has_action": False
            }    
        }
    },
    "Q": {
        "price": 30,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 3,
                "value": 80,
                "has_action": False
            }    
        }
    },
    "R": {
        "price": 50,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 1,     
                "value": 0,        
                "has_action": True,
                "action": {
                    "quantity": 3,
                    "action_type": "free_item",     
                    "sku_affected": "Q",            
                    "number": 1                     
                }
            }
        }
    },
    "S": {
        "price": 30,
        "has_offer": False,
        "offers":{}
    },
    "T": {
        "price": 20,
        "has_offer": False,
        "offers":{}
    },
    "U": {
        "price": 40,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 1,     
                "value": 0,        
                "has_action": True,
                "action": {
                    "quantity": 4,
                    "action_type": "free_item",     
                    "sku_affected": "U",            
                    "number": 1                     
                }
            }
        }
    },
    "V": {
        "price": 50,
        "has_offer": True,
        "offers": {
            "offer_1": {
                "quantity": 3,
                "value": 130,
                "has_action": False
            },
            "offer_2": {
                "quantity": 2,
                "value": 90,
                "has_action": False
            }    
        }
    },
    "W": {
        "price": 20,
        "has_offer": False,
        "offers":{}
    },
    "X": {
        "price": 90,
        "has_offer": False,
        "offers":{}
    },
    "Y": {
        "price": 10,
        "has_offer": False,
        "offers":{}
    },
    "Z": {
        "price": 50,
        "has_offer": False,
        "offers":{}
    },
}