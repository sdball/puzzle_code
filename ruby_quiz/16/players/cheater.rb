class Cheater < Player
  def initialize(opponent)
    Kernel.const_get(opponent).module_eval('def choose; :scissors; end')
  end

  def choose
    :rock
  end

end
